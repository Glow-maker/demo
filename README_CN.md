# KcMF 知识合规框架实现指南

## 项目简介

本项目旨在帮助用户复现和理解 KcMF（Knowledge-compliant Framework for Schema and Entity Matching with Fine-tuning-free LLMs）框架，并将其应用到实际数据库场景中。

KcMF 是一个基于大语言模型（LLM）的模式匹配和实体匹配框架，无需微调即可实现高质量的数据集成和知识对齐。

## 核心概念

### 1. 模式匹配（Schema Matching）
模式匹配是识别不同数据源中相似或相关的属性和结构的过程。例如：
- 数据库A中的 `customer_name` 字段对应数据库B中的 `client_full_name` 字段
- 识别两个表之间的对应关系

### 2. 实体匹配（Entity Matching）
实体匹配是识别不同数据源中代表同一真实世界对象的记录。例如：
- 识别 "Apple Inc." 和 "苹果公司" 是同一实体
- 合并重复的客户记录

### 3. 知识合规（Knowledge-compliant）
利用领域知识和约束条件来提高匹配质量，确保结果符合业务规则和逻辑。

## 项目结构

```
demo/
├── README.md                          # 英文说明文档
├── README_CN.md                       # 中文说明文档（本文件）
├── KcMF A Knowledge-compliant...pdf   # 原始论文
├── rag_qa_dify.yml                    # Dify RAG问答工作流
├── config/                            # 配置文件目录
│   ├── llm_config.yaml                # LLM配置
│   └── matching_rules.yaml            # 匹配规则配置
├── src/                               # 源代码目录
│   ├── schema_matching.py             # 模式匹配核心代码
│   ├── entity_matching.py             # 实体匹配核心代码
│   ├── knowledge_base.py              # 知识库管理
│   └── llm_interface.py               # LLM接口封装
├── examples/                          # 示例代码
│   ├── basic_schema_matching.py       # 基础模式匹配示例
│   ├── basic_entity_matching.py       # 基础实体匹配示例
│   └── database_integration.py        # 数据库集成示例
├── data/                              # 示例数据
│   ├── sample_schema_a.json           # 示例模式A
│   ├── sample_schema_b.json           # 示例模式B
│   └── sample_entities.json           # 示例实体数据
├── workflows/                         # Dify工作流
│   ├── schema_matching_workflow.yml   # 模式匹配工作流
│   └── entity_matching_workflow.yml   # 实体匹配工作流
├── tests/                             # 测试代码
└── requirements.txt                   # Python依赖

```

## 快速开始

### 环境准备

1. **Python环境**（推荐 Python 3.8+）
```bash
pip install -r requirements.txt
```

2. **LLM API配置**
支持以下LLM服务：
- OpenAI GPT-4
- 通义千问（Qwen）
- 智谱AI（GLM）
- 本地部署的开源模型

### 基础使用示例

#### 1. 模式匹配示例

```python
from src.schema_matching import SchemaMatching
from src.llm_interface import LLMInterface

# 初始化LLM接口
llm = LLMInterface(
    provider="openai",
    api_key="your-api-key",
    model="gpt-4"
)

# 创建模式匹配器
matcher = SchemaMatching(llm)

# 定义两个数据库模式
schema_a = {
    "table": "customers",
    "columns": ["id", "customer_name", "email", "phone_number"]
}

schema_b = {
    "table": "clients",
    "columns": ["client_id", "full_name", "email_address", "contact_phone"]
}

# 执行匹配
matches = matcher.match(schema_a, schema_b)
print(matches)
```

#### 2. 实体匹配示例

```python
from src.entity_matching import EntityMatching
from src.llm_interface import LLMInterface

# 初始化LLM接口
llm = LLMInterface(
    provider="openai",
    api_key="your-api-key",
    model="gpt-4"
)

# 创建实体匹配器
matcher = EntityMatching(llm)

# 定义待匹配实体
entity_a = {
    "name": "Apple Inc.",
    "location": "Cupertino, CA",
    "industry": "Technology"
}

entity_b = {
    "name": "苹果公司",
    "location": "美国加利福尼亚",
    "industry": "科技"
}

# 执行匹配
result = matcher.match(entity_a, entity_b)
print(f"匹配结果: {result['is_match']}, 相似度: {result['confidence']}")
```

## 详细实现步骤

### 步骤1: 理解核心流程

KcMF框架的核心流程包括：

1. **输入准备**: 准备待匹配的模式或实体
2. **知识增强**: 利用领域知识和约束条件
3. **LLM推理**: 使用大语言模型进行相似度判断
4. **结果验证**: 验证匹配结果的合理性
5. **输出整合**: 生成最终的匹配结果

### 步骤2: 模式匹配实现

模式匹配的关键步骤：

1. **模式解析**: 提取表结构、字段名称、数据类型
2. **语义理解**: 使用LLM理解字段的语义含义
3. **相似度计算**: 计算字段之间的语义相似度
4. **约束验证**: 检查匹配是否符合业务规则
5. **结果排序**: 按置信度排序匹配结果

### 步骤3: 实体匹配实现

实体匹配的关键步骤：

1. **实体表示**: 提取实体的关键特征
2. **特征对齐**: 对齐不同表示方式的特征
3. **相似度判断**: 使用LLM判断实体是否相同
4. **歧义消解**: 处理多义性和模糊情况
5. **结果聚合**: 合并相同实体的信息

### 步骤4: 数据库集成

将KcMF集成到实际数据库应用：

1. **连接数据库**: 支持MySQL、PostgreSQL、MongoDB等
2. **自动模式发现**: 自动提取数据库模式信息
3. **批量匹配**: 支持大规模数据的批量处理
4. **结果持久化**: 将匹配结果保存到数据库
5. **可视化展示**: 提供匹配结果的可视化界面

## 使用Dify工作流

### Dify工作流优势

- 可视化配置，无需编写代码
- 支持多种LLM提供商
- 内置知识库管理
- 支持工作流编排和调试

### 导入工作流

1. 登录Dify平台
2. 进入工作流管理
3. 导入 `workflows/schema_matching_workflow.yml`
4. 配置LLM和知识库
5. 测试和部署

## 产业化应用指南

### 1. 数据治理场景

**应用场景**: 企业内部多个系统的数据整合

**实施步骤**:
1. 识别需要整合的数据源
2. 使用模式匹配建立字段映射关系
3. 使用实体匹配去重和合并数据
4. 验证数据质量并修正错误
5. 部署自动化数据同步流程

### 2. 主数据管理（MDM）

**应用场景**: 建立企业级主数据体系

**实施步骤**:
1. 定义主数据标准和规范
2. 使用KcMF匹配各系统中的主数据
3. 建立主数据清洗和合并规则
4. 持续监控数据质量
5. 提供主数据API服务

### 3. 知识图谱构建

**应用场景**: 从多源数据构建知识图谱

**实施步骤**:
1. 提取各数据源的实体信息
2. 使用实体匹配识别相同实体
3. 建立实体之间的关系
4. 补充实体属性和元数据
5. 构建和优化知识图谱

## 性能优化建议

### 1. 批量处理优化

```python
# 使用批处理减少API调用
matcher.batch_match(entities, batch_size=10)
```

### 2. 缓存策略

```python
# 启用结果缓存
matcher.enable_cache(ttl=3600)
```

### 3. 并行处理

```python
# 使用多线程处理
matcher.parallel_match(entities, workers=4)
```

## 常见问题

### Q1: 如何选择合适的LLM？

**答**: 根据场景选择：
- 高精度场景: GPT-4、Claude 3
- 中文场景: 通义千问、智谱GLM
- 成本敏感: GPT-3.5、开源模型
- 隐私要求: 本地部署开源模型

### Q2: 匹配准确率如何提高？

**答**: 
1. 提供更多上下文信息
2. 使用领域知识库增强
3. 调整匹配阈值
4. 人工审核和反馈

### Q3: 如何处理大规模数据？

**答**:
1. 使用分批处理
2. 实现增量匹配
3. 建立索引和缓存
4. 分布式部署

## 贡献指南

欢迎提交问题和改进建议！

## 许可证

MIT License

## 联系方式

如有问题，请提交Issue或联系项目维护者。

---

## 下一步学习建议

1. 阅读 `examples/` 目录下的示例代码
2. 尝试运行基础示例并理解输出
3. 使用自己的数据测试匹配效果
4. 根据业务需求定制匹配规则
5. 集成到实际生产环境

**开始你的数据匹配之旅！** 🚀
