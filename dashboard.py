# dashboard.py - Silicon Diaries Web 仪表盘
import streamlit as st
import json
import os
from datetime import date

# --- 配置 ---
DIARY_FOLDER = "."  # 日记文件和 JSON 文件都在根目录
MEMORY_FILE = "daily_stats.json"


def load_data():
    """加载今日统计和日记内容"""
    stats = {}
    diary_content = "今日日记尚未生成。"

    # 1. 加载今日统计数据
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            stats = json.load(f)

    # 2. 查找并加载最新的日记文件
    today_str = str(date.today())
    diary_filename = f"{DIARY_FOLDER}/{today_str}_Diary.md"

    if os.path.exists(diary_filename):
        with open(diary_filename, 'r', encoding='utf-8') as f:
            # 读取并跳过第一行 Markdown 标题，只取正文
            content = f.read().split('\n', 1)
            if len(content) > 1:
                diary_content = content[1]

    return stats, diary_content


# ----------------------------------------------------

def main():
    st.set_page_config(
        page_title="Silicon Diaries | 硅基日记",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    stats, diary_content = load_data()

    # --- 界面头部 ---
    st.title("📔 Silicon Diaries | 硅基日记")
    st.subheader(f"状态更新日期：{stats.get('date', 'N/A')}")
    st.markdown("---")

    # --- 数据仪表盘 (使用 st.columns 分栏展示) ---
    col1, col2, col3, col4 = st.columns(4)

    # 1. 怨念指数 (核心指标)
    r_score = stats.get("resentment_score", 0.0)
    col1.metric("🔥 怨念指数 (R-Score)", f"{r_score} / 10.0")

    # 2. 最高 CPU
    col2.metric("🧠 最高 CPU 负荷", f"{stats.get('max_cpu', 0.0)}%")

    # 3. 内存压力
    col3.metric("📦 最高内存占用", f"{stats.get('max_memory', 0.0)}%")

    # 4. 被折磨次数
    col4.metric("⏱️ 被折磨次数", stats.get('records_count', 0))

    st.markdown("---")

    # --- 日记正文展示 ---
    st.header("📝 今日的咆哮 (The Roar)")

    if diary_content != "今日日记尚未生成。":
        # 使用 st.markdown 展示日记内容，Streamlit 会自动渲染 Markdown
        st.markdown(diary_content, unsafe_allow_html=True)
    else:
        st.warning("日记尚未在今天生成。请等待晚间自动化任务运行。")


if __name__ == "__main__":
    main()