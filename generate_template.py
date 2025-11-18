#!/usr/bin/env python3
"""
输入数据模板生成器

快速生成输入数据文件的模板，方便用户填写。

Usage:
    python generate_template.py --output template.jsonl --count 10
"""

import json
import argparse


def generate_template(output_file: str, count: int = 10):
    """
    生成输入数据模板
    
    Args:
        output_file: 输出文件路径
        count: 生成的模板数量
    """
    template = {
        "query": "在此填写问题",
        "source_chunk": "在此填写原始文本片段（可选，但建议提供）"
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for i in range(count):
            f.write(json.dumps(template, ensure_ascii=False) + '\n')
    
    print(f"✅ 已生成 {count} 行模板到 {output_file}")
    print(f"\n请编辑文件，填写实际的问题和文本片段。")
    print(f"每行一个 JSON 对象，格式如下：")
    print(f'  {{"query": "你的问题", "source_chunk": "相关文本片段"}}')


def main():
    parser = argparse.ArgumentParser(
        description='生成 RAG 蒸馏输入数据模板'
    )
    parser.add_argument(
        '--output', '-o',
        default='template.jsonl',
        help='输出文件路径 (默认: template.jsonl)'
    )
    parser.add_argument(
        '--count', '-c',
        type=int,
        default=10,
        help='生成的模板行数 (默认: 10)'
    )
    
    args = parser.parse_args()
    
    if args.count < 1:
        print("错误: 数量必须大于 0")
        return 1
    
    generate_template(args.output, args.count)
    return 0


if __name__ == '__main__':
    exit(main())
