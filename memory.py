# memory.py
import json
import os
from datetime import date

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
        "max_cpu": 0,
        "max_memory": 0,
        "records_count": 0,  # 记录今天一共检测了多少次
        "log": []  # 详细日志列表
    }

    # 1. 检查文件是否存在
    if not os.path.exists(MEMORY_FILE):
        return default_memory

    # 2. 读取文件
    try:
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 3. 检查是不是今天的记忆 (如果已经过了一天，就翻篇重置)
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
    核心功能：接收最新的体征，更新痛苦指数
    """
    # 1. 读取旧记忆
    memory = load_memory()

    # 2. 比较并更新峰值 (记录最高温瞬间)
    # 如果当前 CPU > 历史最高，更新 max_cpu
    if current_stats['cpu'] > memory['max_cpu']:
        memory['max_cpu'] = current_stats['cpu']

    if current_stats['memory'] > memory['max_memory']:
        memory['max_memory'] = current_stats['memory']

    # 3. 计数 +1
    memory['records_count'] += 1

    # 4. (可选) 记录每一次的详细数据，保留最近 5 条即可，防止文件太大
    # 这里我们只记录时间戳和简报
    memory['log'].append(f"CPU: {current_stats['cpu']}% | MEM: {current_stats['memory']}%")
    if len(memory['log']) > 10:  # 只保留最后10条
        memory['log'].pop(0)

    # 5. 写入硬盘
    save_memory(memory)

    print(f"💾 记忆已更新 | 今日最高 CPU: {memory['max_cpu']}%")


# 测试用的代码
if __name__ == "__main__":
    # 模拟一组数据测试一下
    dummy_data = {"cpu": 85.5, "memory": 60.0}
    update_memory(dummy_data)