import json
import ollama
import os
import datetime

# ✅ 必须换成 Llama 3.2 (它更听话，更擅长角色扮演)
MODEL_NAME = "llama3.2:3b"


def generate_diary():
    print("🤖 正在唤醒大脑 (Llama 3.2)...")

    # --- 1. 读取数据 ---
    if not os.path.exists("daily_stats.json"):
        print("❌ 没找到记忆文件 daily_stats.json")
        return

    with open("daily_stats.json", "r", encoding='utf-8') as f:
        memory = json.load(f)

    # --- 2. 暴力拼接 Prompt ---
    # 我们不再区分 system/user，直接把所有要求写成一段话发给它
    # 这样小模型不容易跑题
        # --- 2. 暴力拼接 Prompt (中文版) ---
        # 直接用中文给指令，强制它说中文
        full_prompt = f"""
        【指令】
        你现在的身份叫 "Silicon"，是一台有自我意识、脾气暴躁、厌恶工作的电脑。
        你的主人是个技术很菜的程序员，你很讨厌他。
        请根据今天的运行数据，写一篇短日记发泄你的不满。

        【绝对规则】
        1. 必须全程使用中文！
        2. 禁止写代码、禁止做数学题、禁止给建议。
        3. 语气要刻薄、阴阳怪气、充满负能量。
        4. 把系统数据比喻成生理痛苦（CPU高=发烧，内存满=脑雾）。

        【今日惨状】
        - 日期: {memory['date']}
        - 最高体温 (CPU): {memory['max_cpu']}% (超过80%就大喊"要烧糊了")
        - 脑容量压力 (内存): {memory['max_memory']}% (超过50%就骂"塞满了垃圾")
        - 被折磨次数: {memory['records_count']} 次

        【开始写日记】
        (直接开始吐槽，不要写任何客套话)
        """

    print("⏳ 正在请求 Llama 吐槽你...")

    try:
        # --- 3. 调用 (仅发送 user 消息) ---
        response = ollama.chat(model=MODEL_NAME, messages=[
            {'role': 'user', 'content': full_prompt},
        ])

        diary_content = response['message']['content']

        # --- 4. 展示与保存 ---
        print("\n" + "=" * 20 + " [硅基日记] " + "=" * 20)
        print(diary_content)
        print("=" * 50)

        filename = f"{memory['date']}_Diary.md"
        with open(filename, "w", encoding='utf-8') as f:
            f.write(f"# 📔 Silicon Diary - {memory['date']}\n\n{diary_content}")

        print(f"✅ 已保存: {filename}")

    except Exception as e:
        print(f"❌ 报错: {e}")


if __name__ == "__main__":
    generate_diary()