# analysis.py
import json
import os
import math

MEMORY_FILE = "daily_stats.json"


def calculate_resentment_score():
    """
    根据当天的峰值数据，计算怨念指数 (0-10分)。
    """
    if not os.path.exists(MEMORY_FILE):
        print("❌ 错误: 找不到记忆文件，无法分析情绪。")
        return 0.0

    try:
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            memory = json.load(f)

        max_cpu = memory.get("max_cpu", 0)
        max_memory = memory.get("max_memory", 0)

        # 定义权重：CPU 60%，内存 40%
        W_CPU = 0.6
        W_MEM = 0.4

        # 标准化评分 (假设 100% CPU/MEM 是满分 10分)
        # 简化公式: (0.6 * MaxCPU + 0.4 * MaxMem) / 10
        raw_score = (W_CPU * max_cpu + W_MEM * max_memory) / 10

        # 将分数限制在 0 到 10 之间，并保留一位小数
        r_score = round(min(raw_score, 10.0), 1)

        print("-" * 30)
        print(f"🧠 怨念指数计算结果: {r_score} / 10.0")
        print(f"   (Max CPU: {max_cpu}%, Max Memory: {max_memory}%)")
        print("-" * 30)

        return r_score

    except Exception as e:
        print(f"⚠️ 分析模块出错: {e}")
        return 0.0


if __name__ == "__main__":
    calculate_resentment_score()