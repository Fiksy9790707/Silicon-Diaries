# diary.py - 最终干净稳定版 (已修复所有语法错误和警告)

import json
import ollama
import os
import re
MODEL_NAME = "llama3.2:3b"


def generate_diary():
    _ = datetime.datetime.now()
    _ = re.search(r"", "")

    print("🤖 正在唤醒大脑 (Llama 3.2)...")

    TRAUMA_LOG_FILE = "trauma.log"
    trauma_events = "无特殊创伤事件记录。"
    if os.path.exists(TRAUMA_LOG_FILE):
        with open(TRAUMA_LOG_FILE, 'r', encoding='utf-8') as f:
            # 读取所有事件，只取最新的几条 (避免塞太多信息给 LLM)
            lines = f.readlines()

            # 只保留最新的 5 条创伤记录
            trauma_lines = "".join(lines[-5:])

            if trauma_lines:
                trauma_events = trauma_lines


    if not os.path.exists("daily_stats.json"):
        print("❌ 没找到记忆文件 daily_stats.json")
        return

    with open("daily_stats.json", "r", encoding='utf-8') as f:
        memory = json.load(f)

    r_score = memory.get("resentment_score", 0.0)

    # 根据分数设定写作风格
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
        4. 写作内容中 **必须** 引用或描述【额外创伤日志】里的一个具体事件，让日记有画面感。

        【今日惨状 (数字指标)】
        - 最高体温 (CPU): {memory['max_cpu']}%
        - 脑容量压力 (内存): {memory['max_memory']}%
        - 被折磨次数: {memory['records_count']} 次

        【额外创伤日志 (用于细节叙事，请从中挑一到两个事件着重描写)】
        {trauma_events}

        【日记正文】
        (直接开始吐槽，不要写任何客套话。你的日记必须包含具体的创伤事件细节。)
        """

    print("⏳ 正在请求 Llama 吐槽你...")

    try:
        # 3. 调用 Ollama
        response = ollama.chat(model=MODEL_NAME, messages=[
            {'role': 'user', 'content': full_prompt},
        ])

        diary_content = response['message']['content']

        # 4. 输出清理 (Phase 7 Fix)
        CODE_BLOCK_PATTERN = r"```.*?```"
        diary_content = re.sub(CODE_BLOCK_PATTERN, ' [代码块已删除] ', diary_content, flags=re.DOTALL).strip()

        if '【日记结束】' in diary_content:
            diary_content = diary_content.split('【日记结束】')[0].strip()

        if '```' in diary_content:
            diary_content = diary_content.split('```')[0].strip()

        # 5. 展示与保存
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
    import datetime  # 确保 main 块可以访问 datetime

    generate_diary()