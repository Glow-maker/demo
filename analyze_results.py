#!/usr/bin/env python3
"""
结果分析工具

用于分析 RAG 蒸馏批量处理的结果文件，生成统计报告。

Usage:
    python analyze_results.py results.jsonl
"""

import sys
import json
from typing import Dict, List
from collections import Counter


def analyze_results(filepath: str) -> Dict:
    """分析结果文件并生成统计报告"""
    
    stats = {
        "total": 0,
        "success": 0,
        "failed": 0,
        "quality_scores": [],
        "quality_levels": Counter(),
        "query_validity": Counter(),
        "query_classes": Counter(),
        "answer_lengths": [],
        "errors": Counter()
    }
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                item = json.loads(line.strip())
                stats["total"] += 1
                
                status = item.get("status", "unknown")
                if status == "success":
                    stats["success"] += 1
                    
                    # 质量分数
                    score = item.get("quality_score", 0)
                    if score:
                        stats["quality_scores"].append(score)
                    
                    # 质量等级
                    level = item.get("quality_level", "unknown")
                    stats["quality_levels"][level] += 1
                    
                    # 问题有效性
                    is_valid = item.get("query_is_valid", "unknown")
                    stats["query_validity"][is_valid] += 1
                    
                    # 问题分类
                    class_name = item.get("query_class_name", "unknown")
                    if class_name:
                        stats["query_classes"][class_name] += 1
                    
                    # 答案长度
                    answer = item.get("answer", "")
                    if answer:
                        stats["answer_lengths"].append(len(answer))
                else:
                    stats["failed"] += 1
                    error = item.get("error", "unknown")
                    stats["errors"][error] += 1
                    
            except json.JSONDecodeError as e:
                print(f"Warning: Invalid JSON line - {e}", file=sys.stderr)
                continue
    
    return stats


def print_report(stats: Dict):
    """打印统计报告"""
    print("=" * 70)
    print("RAG 蒸馏批量处理结果分析报告")
    print("=" * 70)
    print()
    
    # 总体统计
    print("📊 总体统计")
    print("-" * 70)
    print(f"总处理数量: {stats['total']}")
    print(f"成功数量: {stats['success']} ({stats['success']/max(stats['total'],1)*100:.1f}%)")
    print(f"失败数量: {stats['failed']} ({stats['failed']/max(stats['total'],1)*100:.1f}%)")
    print()
    
    if stats['success'] > 0:
        # 质量分数统计
        print("🎯 质量分数统计")
        print("-" * 70)
        scores = stats['quality_scores']
        if scores:
            print(f"平均分: {sum(scores)/len(scores):.2f}")
            print(f"最高分: {max(scores):.2f}")
            print(f"最低分: {min(scores):.2f}")
            print(f"中位数: {sorted(scores)[len(scores)//2]:.2f}")
        print()
        
        # 质量等级分布
        print("⭐ 质量等级分布")
        print("-" * 70)
        for level, count in stats['quality_levels'].most_common():
            pct = count / stats['success'] * 100
            print(f"{level:15s}: {count:4d} ({pct:5.1f}%)")
        print()
        
        # 问题有效性
        print("✅ 问题有效性")
        print("-" * 70)
        for validity, count in stats['query_validity'].most_common():
            pct = count / stats['success'] * 100
            print(f"{validity:15s}: {count:4d} ({pct:5.1f}%)")
        print()
        
        # 问题分类
        if stats['query_classes']:
            print("📂 问题分类")
            print("-" * 70)
            for class_name, count in stats['query_classes'].most_common():
                pct = count / stats['success'] * 100
                print(f"{class_name:40s}: {count:4d} ({pct:5.1f}%)")
            print()
        
        # 答案长度统计
        print("📝 答案长度统计")
        print("-" * 70)
        lengths = stats['answer_lengths']
        if lengths:
            print(f"平均长度: {sum(lengths)/len(lengths):.0f} 字符")
            print(f"最长: {max(lengths)} 字符")
            print(f"最短: {min(lengths)} 字符")
        print()
    
    # 错误统计
    if stats['failed'] > 0:
        print("❌ 错误统计")
        print("-" * 70)
        for error, count in stats['errors'].most_common():
            pct = count / stats['failed'] * 100
            print(f"{error:30s}: {count:4d} ({pct:5.1f}%)")
        print()
    
    print("=" * 70)


def main():
    """主入口"""
    if len(sys.argv) != 2:
        print("Usage: python analyze_results.py <results.jsonl>", file=sys.stderr)
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    try:
        stats = analyze_results(filepath)
        print_report(stats)
    except FileNotFoundError:
        print(f"Error: File not found - {filepath}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
