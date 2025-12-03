# KcMF 生产环境部署指南

本指南介绍如何将 KcMF 框架部署到生产环境，包括性能优化、监控、和运维最佳实践。

## 目录

1. [部署架构](#1-部署架构)
2. [环境准备](#2-环境准备)
3. [配置管理](#3-配置管理)
4. [性能优化](#4-性能优化)
5. [监控和日志](#5-监控和日志)
6. [安全加固](#6-安全加固)
7. [高可用部署](#7-高可用部署)
8. [运维指南](#8-运维指南)

---

## 1. 部署架构

### 1.1 推荐架构

```
┌─────────────────┐
│   负载均衡器     │
│   (Nginx/HAProxy)│
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼───┐ ┌──▼────┐
│ API-1 │ │ API-2 │  (KcMF API服务)
└───┬───┘ └──┬────┘
    │        │
    └────┬───┘
         │
    ┌────▼────┐
    │  Redis  │  (缓存层)
    └────┬────┘
         │
    ┌────▼────────┐
    │ PostgreSQL  │  (结果存储)
    └─────────────┘
```

### 1.2 组件说明

- **API服务**: FastAPI/Flask 应用，处理匹配请求
- **缓存层**: Redis，缓存匹配结果和LLM响应
- **数据库**: 存储配置、日志和历史结果
- **消息队列**: Celery/RabbitMQ，处理异步任务

---

## 2. 环境准备

### 2.1 服务器要求

**最低配置**:
- CPU: 2核
- 内存: 4GB
- 磁盘: 20GB SSD
- 网络: 10Mbps

**推荐配置**:
- CPU: 4核+
- 内存: 8GB+
- 磁盘: 50GB+ SSD
- 网络: 100Mbps+

### 2.2 系统依赖

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y python3.9 python3-pip python3-venv
sudo apt-get install -y postgresql-client redis-tools nginx

# CentOS/RHEL
sudo yum install -y python39 python39-pip
sudo yum install -y postgresql redis nginx
```

### 2.3 Python环境

```bash
# 创建虚拟环境
python3.9 -m venv /opt/kcmf/venv

# 激活环境
source /opt/kcmf/venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 安装生产依赖
pip install gunicorn uvicorn[standard] redis celery
```

---

## 3. 配置管理

### 3.1 环境变量

创建 `/etc/kcmf/env.prod`:

```bash
# LLM配置
OPENAI_API_KEY=sk-your-production-key
LLM_PROVIDER=openai
LLM_MODEL=gpt-4

# 数据库配置
DATABASE_URL=postgresql://kcmf:password@localhost/kcmf_prod

# Redis配置
REDIS_URL=redis://localhost:6379/0

# 应用配置
APP_ENV=production
LOG_LEVEL=INFO
MAX_WORKERS=4

# 安全配置
SECRET_KEY=your-secret-key-here
API_KEY_HEADER=X-API-Key
```

### 3.2 配置文件

创建 `/etc/kcmf/config.yaml`:

```yaml
# 生产配置
app:
  name: kcmf-api
  host: 0.0.0.0
  port: 8000
  workers: 4
  timeout: 120

llm:
  provider: openai
  model: gpt-4
  temperature: 0.3
  max_tokens: 2000
  timeout: 60
  retry_attempts: 3

cache:
  enabled: true
  backend: redis
  ttl: 3600
  max_size: 10000

database:
  pool_size: 10
  max_overflow: 20
  pool_timeout: 30

matching:
  schema_threshold: 0.7
  entity_threshold: 0.8
  batch_size: 10
  max_parallel: 4

monitoring:
  enabled: true
  metrics_port: 9090
  health_check_path: /health
```

---

## 4. 性能优化

### 4.1 API服务优化

创建 `api_server.py`:

```python
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
import redis
import hashlib
import json
from typing import Optional

app = FastAPI(title="KcMF API", version="1.0.0")

# 添加中间件
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Redis连接池
redis_pool = redis.ConnectionPool.from_url(
    os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    max_connections=50
)
redis_client = redis.Redis(connection_pool=redis_pool)

# API认证
async def verify_api_key(x_api_key: str = Header(...)):
    valid_keys = os.getenv("VALID_API_KEYS", "").split(",")
    if x_api_key not in valid_keys:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key

# 缓存装饰器
def cache_result(ttl=3600):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            # 生成缓存键
            cache_key = f"kcmf:{func.__name__}:{hashlib.md5(str(kwargs).encode()).hexdigest()}"
            
            # 检查缓存
            cached = redis_client.get(cache_key)
            if cached:
                return json.loads(cached)
            
            # 执行函数
            result = await func(*args, **kwargs)
            
            # 存入缓存
            redis_client.setex(cache_key, ttl, json.dumps(result))
            
            return result
        return wrapper
    return decorator

@app.post("/api/v1/match/schema")
@cache_result(ttl=3600)
async def match_schema(request: dict, api_key: str = Depends(verify_api_key)):
    """Schema matching endpoint with caching"""
    # 实现细节...
    pass

@app.post("/api/v1/match/entity")
@cache_result(ttl=1800)
async def match_entity(request: dict, api_key: str = Depends(verify_api_key)):
    """Entity matching endpoint with caching"""
    # 实现细节...
    pass

@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy", "timestamp": time.time()}
```

### 4.2 使用Gunicorn部署

创建 `gunicorn_config.py`:

```python
import multiprocessing

# 服务器配置
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
timeout = 120
keepalive = 5

# 日志配置
accesslog = "/var/log/kcmf/access.log"
errorlog = "/var/log/kcmf/error.log"
loglevel = "info"

# 进程命名
proc_name = "kcmf-api"

# 优雅重启
max_requests = 1000
max_requests_jitter = 50
```

启动服务:

```bash
gunicorn api_server:app -c gunicorn_config.py
```

### 4.3 异步任务处理

使用Celery处理批量任务:

```python
# celery_app.py
from celery import Celery

app = Celery('kcmf', broker='redis://localhost:6379/1')

@app.task
def batch_match_schema(schema_pairs):
    """批量匹配模式"""
    results = []
    for schema_a, schema_b in schema_pairs:
        result = matcher.match(schema_a, schema_b)
        results.append(result)
    return results

@app.task
def dedup_entities(entities, threshold=0.8):
    """批量去重实体"""
    matcher = create_entity_matcher(llm, threshold)
    duplicates = matcher.find_duplicates(entities)
    return duplicates
```

启动Celery worker:

```bash
celery -A celery_app worker --loglevel=info --concurrency=4
```

---

## 5. 监控和日志

### 5.1 结构化日志

```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
        }
        
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        return json.dumps(log_data)

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("/var/log/kcmf/app.log")
    ]
)

for handler in logging.root.handlers:
    handler.setFormatter(JSONFormatter())
```

### 5.2 Prometheus监控

```python
from prometheus_client import Counter, Histogram, Gauge, generate_latest

# 定义指标
request_count = Counter('kcmf_requests_total', 'Total requests', ['endpoint', 'status'])
request_duration = Histogram('kcmf_request_duration_seconds', 'Request duration')
cache_hit_rate = Gauge('kcmf_cache_hit_rate', 'Cache hit rate')

@app.middleware("http")
async def monitor_requests(request, call_next):
    with request_duration.time():
        response = await call_next(request)
        request_count.labels(
            endpoint=request.url.path,
            status=response.status_code
        ).inc()
    return response

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type="text/plain")
```

### 5.3 ELK日志聚合

配置 Filebeat (`/etc/filebeat/filebeat.yml`):

```yaml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/kcmf/*.log
    json.keys_under_root: true
    json.add_error_key: true

output.elasticsearch:
  hosts: ["localhost:9200"]
  index: "kcmf-logs-%{+yyyy.MM.dd}"
```

---

## 6. 安全加固

### 6.1 API密钥管理

```python
import secrets
import hashlib

def generate_api_key():
    """生成安全的API密钥"""
    return secrets.token_urlsafe(32)

def hash_api_key(api_key: str) -> str:
    """哈希API密钥用于存储"""
    return hashlib.sha256(api_key.encode()).hexdigest()
```

### 6.2 速率限制

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/api/v1/match/schema")
@limiter.limit("100/minute")
async def match_schema(request: Request):
    # 实现...
    pass
```

### 6.3 数据加密

```python
from cryptography.fernet import Fernet

class DataEncryptor:
    def __init__(self, key: bytes):
        self.cipher = Fernet(key)
    
    def encrypt(self, data: str) -> str:
        return self.cipher.encrypt(data.encode()).decode()
    
    def decrypt(self, encrypted: str) -> str:
        return self.cipher.decrypt(encrypted.encode()).decode()
```

---

## 7. 高可用部署

### 7.1 Docker部署

`Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 安装Python依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制代码
COPY . .

# 创建非root用户
RUN useradd -m -u 1000 kcmf && chown -R kcmf:kcmf /app
USER kcmf

# 健康检查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# 启动服务
CMD ["gunicorn", "api_server:app", "-c", "gunicorn_config.py"]
```

`docker-compose.yml`:

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - REDIS_URL=redis://redis:6379/0
      - DATABASE_URL=postgresql://kcmf:password@postgres/kcmf
    depends_on:
      - redis
      - postgres
    deploy:
      replicas: 2
      resources:
        limits:
          cpus: '1'
          memory: 2G
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    restart: unless-stopped

  postgres:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=kcmf
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=kcmf
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  redis_data:
  postgres_data:
```

### 7.2 Kubernetes部署

`k8s-deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kcmf-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: kcmf-api
  template:
    metadata:
      labels:
        app: kcmf-api
    spec:
      containers:
      - name: api
        image: kcmf-api:latest
        ports:
        - containerPort: 8000
        env:
        - name: REDIS_URL
          valueFrom:
            secretKeyRef:
              name: kcmf-secrets
              key: redis-url
        resources:
          requests:
            cpu: 500m
            memory: 1Gi
          limits:
            cpu: 1000m
            memory: 2Gi
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: kcmf-api-service
spec:
  selector:
    app: kcmf-api
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
  type: LoadBalancer
```

---

## 8. 运维指南

### 8.1 日常监控

```bash
# 检查服务状态
systemctl status kcmf-api

# 查看实时日志
tail -f /var/log/kcmf/app.log

# 检查Redis状态
redis-cli info stats

# 检查数据库连接
psql -U kcmf -d kcmf_prod -c "SELECT count(*) FROM matches;"
```

### 8.2 备份策略

```bash
#!/bin/bash
# backup.sh

BACKUP_DIR="/backup/kcmf"
DATE=$(date +%Y%m%d_%H%M%S)

# 备份数据库
pg_dump -U kcmf kcmf_prod > "$BACKUP_DIR/db_$DATE.sql"

# 备份Redis
redis-cli BGSAVE
cp /var/lib/redis/dump.rdb "$BACKUP_DIR/redis_$DATE.rdb"

# 备份配置
tar czf "$BACKUP_DIR/config_$DATE.tar.gz" /etc/kcmf/

# 保留最近30天的备份
find $BACKUP_DIR -name "*.sql" -mtime +30 -delete
```

### 8.3 故障恢复

```bash
# 1. 停止服务
systemctl stop kcmf-api

# 2. 恢复数据库
psql -U kcmf -d kcmf_prod < backup.sql

# 3. 恢复Redis
cp backup.rdb /var/lib/redis/dump.rdb
systemctl restart redis

# 4. 启动服务
systemctl start kcmf-api

# 5. 验证
curl http://localhost:8000/health
```

### 8.4 性能调优

```bash
# 监控API响应时间
curl -w "@curl-format.txt" -o /dev/null -s http://localhost:8000/api/v1/match/schema

# 查看Redis缓存命中率
redis-cli info stats | grep hit

# 数据库慢查询
psql -U kcmf -c "SELECT * FROM pg_stat_statements ORDER BY mean_exec_time DESC LIMIT 10;"

# 系统资源使用
htop
iostat -x 1
```

---

## 总结

生产环境部署清单：

- [ ] 配置环境变量和密钥
- [ ] 设置Redis缓存
- [ ] 配置数据库连接池
- [ ] 启用API认证和速率限制
- [ ] 配置日志和监控
- [ ] 设置自动备份
- [ ] 配置负载均衡
- [ ] 实施健康检查
- [ ] 编写运维文档
- [ ] 进行压力测试

更多信息请参考：
- [API文档](API.md)
- [监控指南](MONITORING.md)
- [故障排查](TROUBLESHOOTING.md)
