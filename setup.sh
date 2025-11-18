#!/bin/bash
# 快速设置脚本

echo "🚀 RAG QA 蒸馏项目设置"
echo "======================================"
echo ""

# 检查 Python 版本
echo "📌 检查 Python 版本..."
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到 Python 3。请先安装 Python 3.7 或更高版本。"
    exit 1
fi

python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✅ Python 版本: $python_version"
echo ""

# 安装依赖
echo "📦 安装 Python 依赖..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ 依赖安装失败"
    exit 1
fi
echo "✅ 依赖安装完成"
echo ""

# 检查 DIFY_KEY
echo "🔑 检查 API Key..."
if [ -z "$DIFY_KEY" ]; then
    echo "⚠️  警告: DIFY_KEY 环境变量未设置"
    echo ""
    echo "请在 ~/.bashrc 中添加以下行："
    echo "    export DIFY_KEY=\"your-api-key-here\""
    echo ""
    echo "然后运行: source ~/.bashrc"
    echo ""
    echo "或者在运行脚本时使用 --api-key 参数"
else
    echo "✅ DIFY_KEY 已设置"
fi
echo ""

# 设置执行权限
echo "⚙️  设置脚本执行权限..."
chmod +x rag_distillation.py
chmod +x analyze_results.py
echo "✅ 权限设置完成"
echo ""

echo "======================================"
echo "✨ 设置完成！"
echo ""
echo "📖 快速开始:"
echo "  1. 准备输入数据 (JSONL 格式):"
echo "     sample_data.jsonl 是示例文件"
echo ""
echo "  2. 运行批量处理:"
echo "     python3 rag_distillation.py -i sample_data.jsonl -o results.jsonl"
echo ""
echo "  3. 分析结果:"
echo "     python3 analyze_results.py results.jsonl"
echo ""
echo "📚 详细文档请查看 README.md"
echo "======================================"
