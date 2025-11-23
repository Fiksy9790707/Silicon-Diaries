# memory.py - V3.0 (包含 Phase 5 怨念指数计算)

import json
import os
from datetime import date
import analysis  # 确保 analysis.py 文件存在且正确

# 记忆文件的存储路径
MEMORY_FILE = "daily_stats.json"


def load_memory():
    """
    读取记忆文件。如果文件不存在，或者日期不是今天，就重置记忆。
    """
    today_str = str(date.today())

    # 默认的初始记忆（一张白纸）
    default_memory = {
        "date": today_str,
        "max_cpu": 0.0,
        "max_memory": 0.0,
        "records_count": 0,
        "log": []
    }

    if not os.path.exists(MEMORY_FILE):
        return default_memory

    try:
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if data.get("date") != today_str:
            print("📅 新的一天开始了，重置记忆...")
            return default_memory

        return data
    except Exception as e:
        print(f"⚠️ 记忆读取出错: {e}, 重置记忆。")
        return default_memory


def save_memory(memory_data):
    """
    把记忆写回硬盘
    """
    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(memory_data, f, indent=4, ensure_ascii=False)


def update_memory(current_stats):
    """
    核心功能：接收最新的体征，更新痛苦指数，并计算 R-Score
    """
    # 1. 读取旧记忆
    memory = load_memory()

    # 2. 比较并更新峰值
    if current_stats['cpu'] > memory['max_cpu']:
        memory['max_cpu'] = current_stats['cpu']

    if current_stats['memory'] > memory['max_memory']:
        memory['max_memory'] = current_stats['memory']

    # 3. 计数 +1
    memory['records_count'] += 1

    # 4. 记录日志 (保留最近 10 条)
    memory['log'].append(
        f"{datetime.datetime.now().strftime('%H:%M')} | CPU: {current_stats['cpu']}% | MEM: {current_stats['memory']}%")
    if len(memory['log']) > 10:
        memory['log'].pop(0)

    # 5. 计算怨念指数并保存
    # 先保存一次，确保 analysis.py 读取到最新的 max 值
    save_memory(memory)

    # 6. 计算分数
    r_score = analysis.calculate_resentment_score()
    memory['resentment_score'] = r_score

    # 7. 最终保存
    save_memory(memory)

    print(f"💾 记忆已更新 | 今日最高 CPU: {memory['max_cpu']}% | R-Score: {r_score}")


# 测试用的代码
if __name__ == "__main__":
    # ⚠️ 注意：这里需要导入 datetime 才能使用 datetime.datetime.now()
    import datetime

    # 模拟一组数据测试一下
    dummy_data = {"cpu": 85.5, "memory": 60.0}
    update_memory(dummy_data)