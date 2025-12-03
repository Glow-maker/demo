# KcMF 实现教程：从入门到产业化

本教程将引导您逐步理解和实现 KcMF（Knowledge-compliant Framework for Schema and Entity Matching with Fine-tuning-free LLMs）框架。

## 目录

1. [核心概念理解](#1-核心概念理解)
2. [环境搭建](#2-环境搭建)
3. [第一步：模式匹配基础](#3-第一步模式匹配基础)
4. [第二步：实体匹配基础](#4-第二步实体匹配基础)
5. [第三步：使用Dify工作流](#5-第三步使用dify工作流)
6. [第四步：数据库集成](#6-第四步数据库集成)
7. [第五步：产业化部署](#7-第五步产业化部署)
8. [常见问题和最佳实践](#8-常见问题和最佳实践)

---

## 1. 核心概念理解

### 1.1 什么是模式匹配（Schema Matching）？

**定义**：模式匹配是识别不同数据源中相似或相关的数据结构（表、字段）的过程。

**现实场景**：
```
公司A的数据库：
  customers 表
    - customer_id (客户ID)
    - customer_name (客户名称)
    - email (邮箱)

公司B的数据库：
  clients 表
    - client_id (客户ID)
    - full_name (全名)
    - email_address (电子邮件)

模式匹配的任务：识别 customer_name ↔ full_name, email ↔ email_address
```

### 1.2 什么是实体匹配（Entity Matching）？

**定义**：实体匹配是识别不同数据源中代表同一真实世界对象的记录。

**现实场景**：
```
数据源A：
  {name: "Apple Inc.", location: "Cupertino, CA"}

数据源B：
  {name: "苹果公司", location: "美国加州库比蒂诺"}

实体匹配的任务：识别这两条记录指向同一家公司
```

### 1.3 为什么使用LLM？

传统方法的局限：
- 基于规则：难以处理复杂变化
- 基于机器学习：需要大量标注数据和训练

LLM的优势：
- ✅ 理解语义：不仅看字面相似，理解含义
- ✅ 跨语言：自动处理中英文等多语言
- ✅ 零微调：无需训练，直接使用
- ✅ 推理能力：可以解释匹配原因

---

## 2. 环境搭建

### 2.1 系统要求

- Python 3.8 或更高版本
- 2GB 以上内存
- 稳定的网络连接（调用LLM API）

### 2.2 安装步骤

```bash
# 1. 克隆项目
git clone <repository-url>
cd demo

# 2. 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置API密钥
cp config/llm_config.yaml.example config/llm_config.yaml
# 编辑 config/llm_config.yaml，填入你的API密钥
```

### 2.3 获取LLM API密钥

#### 选项1：OpenAI（推荐用于测试）
1. 访问 https://platform.openai.com/
2. 注册账号并充值
3. 创建API密钥
4. 配置环境变量：
   ```bash
   export OPENAI_API_KEY='your-key-here'
   ```

#### 选项2：通义千问（推荐用于中文场景）
1. 访问 https://dashscope.aliyun.com/
2. 注册阿里云账号
3. 开通DashScope服务
4. 获取API密钥

#### 选项3：智谱AI（国产替代）
1. 访问 https://open.bigmodel.cn/
2. 注册并获取API密钥

---

## 3. 第一步：模式匹配基础

### 3.1 理解问题

假设您有两个系统：
- **系统A**：老的客户管理系统
- **系统B**：新的CRM系统

需要将数据从A迁移到B，但字段名不同。

### 3.2 运行第一个例子

```bash
cd examples
python basic_schema_matching.py
```

### 3.3 理解代码

打开 `examples/basic_schema_matching.py`，核心代码：

```python
# 1. 创建LLM接口
llm = create_llm(provider="openai", api_key="your-key")

# 2. 创建模式匹配器
matcher = create_schema_matcher(llm, similarity_threshold=0.7)

# 3. 定义两个模式
schema_a = {
    "table": "customers",
    "columns": ["customer_id", "customer_name", "email"]
}

schema_b = {
    "table": "clients",
    "columns": ["client_id", "full_name", "email_address"]
}

# 4. 执行匹配
matches = matcher.match(schema_a, schema_b)

# 5. 查看结果
for match in matches:
    print(f"{match['source_column']['name']} → {match['target_column']['name']}")
    print(f"置信度: {match['confidence']:.2%}")
```

### 3.4 自己动手实践

**练习1**：修改示例中的字段名，看看匹配结果如何变化

```python
# 尝试更复杂的例子
schema_a = {
    "columns": [
        {"name": "usr_id", "type": "INT"},
        {"name": "usr_nm", "type": "VARCHAR"},
        {"name": "reg_dt", "type": "DATE"}
    ]
}

schema_b = {
    "columns": [
        {"name": "user_identifier", "type": "INTEGER"},
        {"name": "username", "type": "TEXT"},
        {"name": "registration_date", "type": "TIMESTAMP"}
    ]
}
```

**练习2**：添加字段描述，观察匹配准确率提升

```python
schema_a = {
    "columns": [
        {
            "name": "qty",
            "type": "INT",
            "description": "库存数量"  # 添加描述
        }
    ]
}
```

---

## 4. 第二步：实体匹配基础

### 4.1 理解场景

**场景**：公司从多个渠道收集客户信息，存在重复记录。

```
来源A：张三，电话：138****1234
来源B：张三，邮箱：zhangsan@example.com
来源C：Zhang San，电话：138-****-1234
```

需要识别这些是同一个人。

### 4.2 运行实体匹配例子

```bash
python basic_entity_matching.py
```

### 4.3 理解核心逻辑

```python
# 1. 创建实体匹配器
matcher = create_entity_matcher(llm, match_threshold=0.8)

# 2. 定义两个实体
entity_a = {
    "name": "Apple Inc.",
    "location": "Cupertino, CA"
}

entity_b = {
    "name": "苹果公司",
    "location": "美国加州库比蒂诺"
}

# 3. 执行匹配
result = matcher.match(entity_a, entity_b)

# 4. 判断是否匹配
if result['is_match']:
    print(f"匹配！置信度：{result['confidence']:.2%}")
else:
    print("不匹配")
```

### 4.4 批量去重

```python
# 找出重复实体
entities = [
    {"name": "Microsoft", "location": "Redmond"},
    {"name": "微软", "location": "雷德蒙德"},
    {"name": "Google", "location": "Mountain View"}
]

duplicate_groups = matcher.find_duplicates(entities)
print(f"发现 {len(duplicate_groups)} 组重复")
```

### 4.5 实践练习

**练习1**：处理人员信息去重

```python
employees = [
    {"name": "John Smith", "email": "john.smith@company.com"},
    {"name": "J. Smith", "email": "jsmith@company.com"},
    {"name": "John M. Smith", "email": "john.smith@company.com"}
]

# 找出重复员工
duplicates = matcher.find_duplicates(employees, context="员工记录")
```

**练习2**：合并重复记录

```python
# 合并重复实体
merged = matcher.merge_entities(duplicates[0], strategy="llm")
print("合并后的记录：", merged)
```

---

## 5. 第三步：使用Dify工作流

### 5.1 什么是Dify？

Dify是一个可视化的LLM应用开发平台，无需编码即可构建工作流。

### 5.2 导入工作流

1. 登录Dify平台：https://cloud.dify.ai/
2. 创建新应用 → 选择"工作流"
3. 导入配置文件：`workflows/schema_matching_workflow.yml`

### 5.3 配置工作流

1. **配置LLM节点**：
   - 选择模型（GPT-4 或 通义千问）
   - 填入API密钥

2. **测试工作流**：
   - 输入示例数据
   - 查看匹配结果

### 5.4 工作流优势

相比纯代码：
- ✅ 可视化调试
- ✅ 方便非技术人员使用
- ✅ 支持版本控制
- ✅ 内置监控和日志

### 5.5 自定义工作流

您可以基于模板创建自己的工作流：
- 添加数据验证节点
- 添加人工审核环节
- 集成到现有系统

---

## 6. 第四步：数据库集成

### 6.1 连接真实数据库

创建文件 `examples/database_integration.py`：

```python
from src import create_llm, create_schema_matcher
import sqlalchemy as sa

# 1. 连接数据库
engine_a = sa.create_engine('mysql://user:pass@host/db_a')
engine_b = sa.create_engine('postgresql://user:pass@host/db_b')

# 2. 提取模式信息
def extract_schema(engine, table_name):
    inspector = sa.inspect(engine)
    columns = inspector.get_columns(table_name)
    return {
        "table": table_name,
        "columns": [
            {
                "name": col["name"],
                "type": str(col["type"]),
                "nullable": col.get("nullable", True)
            }
            for col in columns
        ]
    }

schema_a = extract_schema(engine_a, 'customers')
schema_b = extract_schema(engine_b, 'clients')

# 3. 执行匹配
llm = create_llm("openai")
matcher = create_schema_matcher(llm)
matches = matcher.match(schema_a, schema_b)

# 4. 生成映射SQL
for match in matches:
    source = match['source_column']['name']
    target = match['target_column']['name']
    print(f"{target} = {source}  -- 置信度: {match['confidence']:.2%}")
```

### 6.2 自动化数据迁移

```python
# 基于匹配结果生成INSERT语句
def generate_migration_sql(matches, source_table, target_table):
    source_cols = [m['source_column']['name'] for m in matches]
    target_cols = [m['target_column']['name'] for m in matches]
    
    sql = f"""
    INSERT INTO {target_table} ({', '.join(target_cols)})
    SELECT {', '.join(source_cols)}
    FROM {source_table}
    """
    return sql
```

---

## 7. 第五步：产业化部署

### 7.1 性能优化

#### 批量处理
```python
# 不推荐：逐个处理（慢）
for entity in entities:
    result = matcher.match(entity, target)

# 推荐：批量处理（快）
results = matcher.match_batch(entity_pairs)
```

#### 缓存策略
```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def cached_match(entity_a_json, entity_b_json):
    entity_a = json.loads(entity_a_json)
    entity_b = json.loads(entity_b_json)
    return matcher.match(entity_a, entity_b)
```

### 7.2 错误处理

```python
def robust_match(entity_a, entity_b, max_retries=3):
    for attempt in range(max_retries):
        try:
            return matcher.match(entity_a, entity_b)
        except Exception as e:
            if attempt == max_retries - 1:
                # 最后一次尝试失败，记录日志
                logging.error(f"匹配失败: {e}")
                return None
            time.sleep(2 ** attempt)  # 指数退避
```

### 7.3 监控和日志

```python
import logging
from datetime import datetime

def match_with_logging(entity_a, entity_b):
    start_time = datetime.now()
    
    try:
        result = matcher.match(entity_a, entity_b)
        duration = (datetime.now() - start_time).total_seconds()
        
        logging.info(f"匹配成功，耗时: {duration}s, 置信度: {result['confidence']}")
        return result
    
    except Exception as e:
        logging.error(f"匹配失败: {str(e)}")
        raise
```

### 7.4 API服务化

使用FastAPI创建REST API：

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class MatchRequest(BaseModel):
    entity_a: dict
    entity_b: dict
    context: str = None

@app.post("/api/match")
async def match_entities(request: MatchRequest):
    try:
        result = matcher.match(
            request.entity_a,
            request.entity_b,
            request.context
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 启动服务
# uvicorn api:app --host 0.0.0.0 --port 8000
```

### 7.5 容器化部署

创建 `Dockerfile`：

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```

部署：
```bash
docker build -t kcmf-api .
docker run -p 8000:8000 -e OPENAI_API_KEY=your-key kcmf-api
```

---

## 8. 常见问题和最佳实践

### 8.1 如何提高匹配准确率？

1. **提供更多上下文**
   ```python
   context = "这是金融行业的客户数据，包含交易信息"
   matches = matcher.match(schema_a, schema_b, context=context)
   ```

2. **使用字段描述**
   ```python
   {
       "name": "amt",
       "description": "交易金额，单位为元"  # 关键！
   }
   ```

3. **选择合适的模型**
   - 中文场景：优先通义千问
   - 需要推理：GPT-4
   - 成本敏感：GPT-3.5

### 8.2 如何控制成本？

1. **使用缓存**
2. **批量处理**
3. **设置合理的threshold**（减少不必要的匹配）
4. **使用更便宜的模型做初筛**

### 8.3 如何处理大规模数据？

1. **分批处理**
   ```python
   batch_size = 100
   for i in range(0, len(entities), batch_size):
       batch = entities[i:i+batch_size]
       process_batch(batch)
   ```

2. **并行处理**
   ```python
   from concurrent.futures import ThreadPoolExecutor
   
   with ThreadPoolExecutor(max_workers=4) as executor:
       results = executor.map(process_entity, entities)
   ```

3. **使用数据库索引**
4. **实施增量更新策略**

### 8.4 如何确保数据安全？

1. **不要将敏感数据发送到公共API**
2. **考虑使用本地部署的模型**
3. **数据脱敏处理**
   ```python
   # 匿名化示例
   entity = {
       "name": "张三",
       "id": "hash(real_id)",  # 使用哈希替代真实ID
       "phone": "138****1234"   # 部分掩码
   }
   ```

### 8.5 集成到现有系统

#### 作为定时任务
```python
# cron: 每天凌晨2点执行
0 2 * * * /path/to/venv/bin/python /path/to/match_script.py
```

#### 作为数据流处理
```python
# 使用Apache Kafka
from kafka import KafkaConsumer, KafkaProducer

consumer = KafkaConsumer('new_entities')
producer = KafkaProducer('matched_entities')

for message in consumer:
    entity = json.loads(message.value)
    result = matcher.match(entity, existing_entities)
    producer.send('matched_entities', json.dumps(result))
```

---

## 总结

您现在已经掌握了：

1. ✅ KcMF框架的核心概念
2. ✅ 模式匹配和实体匹配的实现
3. ✅ 使用Dify工作流简化开发
4. ✅ 数据库集成和真实场景应用
5. ✅ 产业化部署的最佳实践

**下一步建议**：

1. 使用您自己的数据测试
2. 根据业务需求调整参数
3. 监控性能和成本
4. 持续优化匹配规则

**需要帮助？**

- 查看示例代码：`examples/` 目录
- 参考API文档：`docs/API.md`
- 提交Issue：GitHub Issues

祝您的数据匹配项目成功！🎉
