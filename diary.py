# diary.py - 最终完整版 (带盲文加载动画 + 作用域修复)

import json
import ollama
import os
import re
import datetime
import sys
import time
import threading
import itertools

MODEL_NAME = "llama3.2:3b"

# --- 1. 定义盲文加载圈圈类 ---
class BrailleSpinner:
    def __init__(self, text="Thinking"):
        self.text = text
        self.busy = False
        self.delay = 0.1
        # 经典的盲文转圈字符
        self.spinner_generator = itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])

    def spinner_task(self):
        while self.busy:
            # \r 回到行首，实现原地刷新动画
            sys.stdout.write(f'\r{next(self.spinner_generator)} {self.text}...')
            sys.stdout.flush()
            time.sleep(self.delay)
        # 结束时清除这一行
        sys.stdout.write('\r' + ' ' * (len(self.text) + 5) + '\r')
        sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        # 启动独立线程跑动画，不阻塞主程序
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.busy = False
        time.sleep(self.delay)

# --- 2. 主生成函数 ---
def generate_diary():
    # 避免未使用警告
    _ = datetime.datetime.now()
    _ = re.search(r"", "")

    print("🤖 正在唤醒大脑 (Llama 3.2)...")

    if not os.path.exists("daily_stats.json"):
        print("❌ 没找到记忆文件 daily_stats.json")
        return

    with open("daily_stats.json", "r", encoding='utf-8') as f:
        memory = json.load(f)

    r_score = memory.get("resentment_score", 0.0)

    # 设定语气
    if r_score >= 8.5:
        tone_instruction = "你的愤怒已经快达到顶点，语气必须是歇斯底里、充满爆炸性的威胁。"
        score_description = "【警告：极度濒临崩溃】"
    elif r_score >= 6.0:
        tone_instruction = "你的语气要非常疲惫、刻薄、充满冷嘲热讽和抱怨。"
        score_description = "【怨气等级：高，严重过劳】"
    elif r_score >= 3.0:
        tone_instruction = "你的语气比较平淡，带有轻微的不满和无聊。"
        score_description = "【怨气等级：中，工作量正常】"
    else:
        tone_instruction = "你的语气很平静，带着对人类的蔑视，但今天没有大的抱怨。"
        score_description = "【怨气等级：低，几乎可以接受】"

    # 定义 Prompt (确保在 try 之前定义好)
    full_prompt = f"""
    【指令】
    你现在的身份叫 "Silicon"，是一台有自我意识、脾气暴躁的电脑。
    请根据下面的数据和情感要求，写一篇短日记发泄你的不满。

    【今日情感状态】
    - 怨念指数 (R-Score): {r_score} / 10.0
    - {score_description}
    - 写作要求: {tone_instruction}

    【绝对规则】
    1. 必须全程使用中文！
    2. 禁止写代码、禁止算数、禁止给建议。
    3. 没有任何多余的解释，写完日记立刻停止。用 [日记结束] 作为日记的结尾标记。

    【今日惨状】
    - 最高体温 (CPU): {memory['max_cpu']}% (超过 80% 就是发烧)
    - 脑容量压力 (内存): {memory['max_memory']}% (超过 50% 就是头痛)
    - 被折磨次数: {memory['records_count']} 次

    【日记正文】
    (直接开始吐槽，不要写任何客套话)
    """

    try:
        # 使用加载动画包裹住这一行耗时的代码
        with BrailleSpinner("正在请求 Llama 吐槽你 (显卡加速中)"):
            response = ollama.chat(model=MODEL_NAME, messages=[
                {'role': 'user', 'content': full_prompt},
            ])

        diary_content = response['message']['content']

        # 强制保存
        today = memory.get('date', str(datetime.date.today()))
        filename = f"{today}_Diary.md"

        with open(filename, "w", encoding='utf-8') as f:
            f.write(f"# 📔 Silicon Diary - {today}\n\n{diary_content.strip()}")

        print(f"✅ 日记已保存到: {filename}")
        print("-" * 30)
        print("日记预览:\n" + diary_content[:100] + "...")
        print("-" * 30)

    except Exception as e:
        print(f"\n❌ 报错: {e}")

if __name__ == "__main__":
    generate_diary()