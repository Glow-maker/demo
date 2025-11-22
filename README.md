# RAG QA Dify 工作流优化项目

## 🎯 项目概述

本项目对 Dify RAG 工作流进行了深度分析和优化，提供了可直接用于生产环境的完整解决方案。

## 📦 快速开始

**推荐使用**: `rag_qa_dify_complete.yml` （完全优化版本）

1. 在 Dify 中导入 `rag_qa_dify_complete.yml`
2. 配置你的知识库ID
3. 测试运行
4. 开始生成高质量的RAG QA对！

## 📚 文档导航

- **[问题解答.md](./问题解答.md)** - 直接回答你的问题（中文，推荐首先阅读）
- **[README_WORKFLOW.md](./README_WORKFLOW.md)** - 项目完整说明
- **[QUICK_COMPARISON.md](./QUICK_COMPARISON.md)** - 三个版本快速对比
- **[RAG_WORKFLOW_ANALYSIS.md](./RAG_WORKFLOW_ANALYSIS.md)** - 详细问题分析
- **[RAG_WORKFLOW_OPTIMIZATION_GUIDE.md](./RAG_WORKFLOW_OPTIMIZATION_GUIDE.md)** - 实施指南

## 🚀 主要改进

✅ 修复 source_chunk 使用问题  
✅ 添加质量评分机制（0-100分）  
✅ 优化 Temperature 参数  
✅ 提升知识检索 top_k  
✅ 修复变量传递问题  
✅ 完整的文档和指南  

## 📊 三个版本

| 版本 | 文件 | 说明 | 推荐度 |
|------|------|------|--------|
| 原始 | rag_qa_dify.yml | 保留参考 | ❌ |
| 部分优化 | rag_qa_dify_optimized.yml | 需手动配置 | ⚠️ |
| 完全优化 | rag_qa_dify_complete.yml | 可直接使用 | ✅ **推荐** |

## 💡 使用建议

1. 直接使用 `rag_qa_dify_complete.yml`
2. 阅读 `问题解答.md` 了解详情
3. 参考 `RAG_WORKFLOW_OPTIMIZATION_GUIDE.md` 进行定制
4. 只使用质量分数 ≥70 的 QA 对

## ✨ 关键特性

- **自动质量评分**: 每个QA对都有0-100的质量分数
- **完整上下文**: source_chunk在所有关键节点中正确使用
- **优化成本**: 降低API调用成本约15%
- **生产就绪**: 可以直接用于生产环境

---

**现在就开始使用吧！** 🚀