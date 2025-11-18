# RAG QA Distillation Project

这个项目提供了一个批量处理工具，用于通过 Dify 工作流进行 RAG（检索增强生成）问答蒸馏，生成高质量的训练数据。

## 功能特点

- 批量处理问题和原始文本片段
- 通过 Dify 工作流生成高质量问答对
- 自动质量评分和分级
- 支持断点续传
- 完整的错误处理和日志记录
- 流式输出结果（实时保存）

## 工作流说明

Dify 工作流配置保存在 `rag_qa_dify.yml` 文件中，包含以下主要功能：

1. **问题合格判断**：评估问题是否可以基于给定上下文回答
2. **问题分类**：区分航天领域问题和通用问题
3. **知识检索**：从知识库检索相关信息
4. **答案生成**：使用大模型生成高质量回答
5. **质量校验**：通过多轮循环验证和改写，确保答案准确性
6. **质量评分**：对生成的 QA 对进行质量评估

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置

### 设置 API Key

在你的 `~/.bashrc` 或 `~/.bash_profile` 中添加：

```bash
export DIFY_KEY="your-dify-api-key-here"
```

然后重新加载配置：

```bash
source ~/.bashrc
```

或者在运行脚本时直接指定：

```bash
python rag_distillation.py --api-key your-dify-api-key-here --input data.jsonl --output results.jsonl
```

## 使用方法

### 准备输入数据

创建一个 JSONL 文件（每行一个 JSON 对象），包含以下字段：

```jsonl
{"query": "你的问题", "source_chunk": "原始文本片段"}
{"query": "另一个问题", "source_chunk": "另一个文本片段"}
```

示例文件 `sample_data.jsonl` 已包含在项目中。

### 运行批量处理

基本用法：

```bash
python rag_distillation.py --input sample_data.jsonl --output results.jsonl
```

完整参数：

```bash
python rag_distillation.py \
  --input data.jsonl \           # 输入文件路径
  --output results.jsonl \       # 输出文件路径
  --delay 1.0 \                  # 请求间隔（秒），默认 1.0
  --api-key YOUR_KEY \           # API Key（可选，默认使用 DIFY_KEY 环境变量）
  --base-url https://api.dify.ai/v1 \  # API 基础 URL
  --no-resume                    # 不使用断点续传（重新开始）
```

### 输出格式

输出 JSONL 文件包含以下字段：

```json
{
  "query": "问题文本",
  "source_chunk": "原始文本片段",
  "answer": "生成的完整答案（包含思维链）",
  "quality_score": 85.5,
  "quality_level": "excellent",
  "quality_details": "质量评分详情",
  "query_is_valid": "true",
  "query_class_name": "与航天领域直接或间接相关的问题",
  "first_rag_answer": "初始生成的答案",
  "distill_rag": [...],
  "timestamp": "2024-01-01T00:00:00",
  "status": "success"
}
```

质量等级：
- `excellent`: 分数 >= 85
- `good`: 分数 >= 70
- `fair`: 分数 >= 55
- `poor`: 分数 < 55

## 特性说明

### 断点续传

脚本支持断点续传功能。如果处理过程中断，再次运行相同命令时会自动跳过已处理的项目：

```bash
# 第一次运行
python rag_distillation.py --input data.jsonl --output results.jsonl

# 如果中断，再次运行会从中断处继续
python rag_distillation.py --input data.jsonl --output results.jsonl
```

如果需要重新开始，使用 `--no-resume` 参数。

### 流式输出

结果会实时写入输出文件，即使处理过程中断，已完成的结果也会被保存。

### 速率控制

使用 `--delay` 参数控制请求间隔，避免超出 API 速率限制：

```bash
python rag_distillation.py --input data.jsonl --output results.jsonl --delay 2.0
```

## 示例

处理示例数据：

```bash
# 使用环境变量中的 API Key
python rag_distillation.py --input sample_data.jsonl --output sample_results.jsonl

# 指定 API Key
python rag_distillation.py \
  --input sample_data.jsonl \
  --output sample_results.jsonl \
  --api-key sk-xxxxx \
  --delay 1.5
```

## 故障排除

### API Key 未找到

```
Error: API key not found. Please set DIFY_KEY environment variable or use --api-key option
```

解决方案：
1. 设置环境变量：`export DIFY_KEY="your-key"`
2. 或使用 `--api-key` 参数

### 连接超时

如果遇到超时错误，可以：
1. 增加请求间隔：`--delay 2.0`
2. 检查网络连接
3. 检查 Dify API 服务状态

### 输入文件格式错误

确保输入文件是有效的 JSONL 格式（每行一个 JSON 对象），且包含 `query` 和 `source_chunk` 字段。

## 项目结构

```
.
├── README.md                 # 项目文档
├── rag_qa_dify.yml          # Dify 工作流配置
├── rag_distillation.py      # 批量处理脚本
├── sample_data.jsonl        # 示例输入数据
└── requirements.txt         # Python 依赖
```

## 许可证

MIT