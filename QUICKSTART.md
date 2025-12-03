# KcMF 快速开始指南 (5分钟入门)

这是一个5分钟快速入门指南，帮助您立即开始使用 KcMF 框架。

## 第一步：安装依赖（1分钟）

```bash
# 克隆项目（如果还没有）
git clone <repository-url>
cd demo

# 安装Python依赖
pip install openai pyyaml python-dotenv

# 注意：完整依赖请看 requirements.txt
# 但对于快速测试，上面这些就足够了
```

## 第二步：配置API密钥（1分钟）

选择以下方式之一：

### 方式1：环境变量（推荐用于测试）

```bash
export OPENAI_API_KEY='your-api-key-here'
```

### 方式2：配置文件（推荐用于生产）

```bash
cp config/llm_config.yaml.example config/llm_config.yaml
# 编辑 config/llm_config.yaml，填入您的API密钥
```

## 第三步：运行第一个例子（3分钟）

### 示例1：模式匹配

创建文件 `test_schema.py`:

```python
import os
import sys
sys.path.insert(0, 'src')

from llm_interface import create_llm
from schema_matching import SchemaMatching

# 1. 创建LLM接口
llm = create_llm(provider="openai", api_key=os.getenv("OPENAI_API_KEY"))

# 2. 创建模式匹配器
matcher = SchemaMatching(llm)

# 3. 定义两个模式
schema_a = {
    "table": "customers",
    "columns": ["id", "name", "email", "phone"]
}

schema_b = {
    "table": "clients", 
    "columns": ["client_id", "full_name", "email_address", "contact_phone"]
}

# 4. 执行匹配
print("正在匹配模式...")
matches = matcher.match(schema_a, schema_b)

# 5. 显示结果
for match in matches:
    print(f"\n匹配发现:")
    print(f"  {match['source_column']['name']} → {match['target_column']['name']}")
    print(f"  置信度: {match['confidence']:.2%}")
    print(f"  原因: {match['reasoning']}")
```

运行：
```bash
python test_schema.py
```

### 示例2：实体匹配

创建文件 `test_entity.py`:

```python
import os
import sys
sys.path.insert(0, 'src')

from llm_interface import create_llm
from entity_matching import EntityMatching

# 1. 创建LLM接口
llm = create_llm(provider="openai", api_key=os.getenv("OPENAI_API_KEY"))

# 2. 创建实体匹配器
matcher = EntityMatching(llm)

# 3. 定义两个实体
company_a = {
    "name": "Apple Inc.",
    "location": "Cupertino, California"
}

company_b = {
    "name": "苹果公司",
    "location": "美国加州库比蒂诺"
}

# 4. 执行匹配
print("正在匹配实体...")
result = matcher.match(company_a, company_b)

# 5. 显示结果
if result['is_match']:
    print(f"\n✓ 匹配！")
    print(f"  置信度: {result['confidence']:.2%}")
    print(f"  原因: {result['reasoning']}")
else:
    print(f"\n✗ 不匹配")
    print(f"  原因: {result['reasoning']}")
```

运行：
```bash
python test_entity.py
```

## 使用内置示例

我们提供了完整的示例代码：

```bash
# 基础模式匹配示例
python examples/basic_schema_matching.py

# 基础实体匹配示例
python examples/basic_entity_matching.py

# 数据库集成示例
python examples/database_integration.py
```

## 常见问题

### Q: 没有API密钥怎么办？

**A**: 您需要注册以下任一服务：
- OpenAI: https://platform.openai.com/
- 通义千问: https://dashscope.aliyun.com/
- 智谱AI: https://open.bigmodel.cn/

大多数服务都提供免费试用额度。

### Q: 可以使用其他LLM吗？

**A**: 可以！只需更改provider参数：

```python
# 使用通义千问
llm = create_llm(provider="qwen", api_key="your-qwen-key")

# 使用智谱GLM
llm = create_llm(provider="glm", api_key="your-glm-key")
```

### Q: 如何提高匹配准确度？

**A**: 三个技巧：
1. 提供更详细的字段描述
2. 添加上下文信息
3. 调整相似度阈值

```python
# 添加字段描述
schema = {
    "columns": [
        {
            "name": "qty",
            "type": "INT",
            "description": "库存数量"  # 添加这个！
        }
    ]
}

# 添加上下文
matches = matcher.match(
    schema_a, 
    schema_b, 
    context="这是电商系统的库存数据"  # 添加这个！
)

# 调整阈值
matcher = SchemaMatching(llm, similarity_threshold=0.8)  # 默认0.7
```

### Q: 报错了怎么办？

**A**: 检查以下几点：
1. API密钥是否正确设置
2. 网络连接是否正常
3. API额度是否充足
4. Python版本是否 >= 3.8

## 下一步学习

恭喜！您已经完成了快速入门。接下来：

1. 📖 阅读[完整教程](docs/TUTORIAL.md)
2. 🔧 了解[部署指南](docs/DEPLOYMENT.md)
3. 💡 尝试用您自己的数据
4. 🚀 集成到生产环境

## 获取帮助

- 查看[中文文档](README_CN.md)
- 查看[英文文档](README.md)
- 查看示例代码：`examples/` 目录
- 提交Issue到GitHub

祝您使用愉快！🎉
