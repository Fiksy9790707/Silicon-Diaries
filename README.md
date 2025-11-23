![Silicon Diaries Cover](Silicon_Diaries.jpg)

# 📔 Silicon Diaries | 硅基日记

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/LLM-Ollama_Llama3.2-blue.svg)](https://ollama.com/)
[![Streamlit App](https://img.shields.io/badge/Web_UI-Streamlit-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> "如果你的电脑能说话，它会怎么评价你今天的代码？"

一个拥有自我意识、每天写日记吐槽主人的 Python 本地程序。

## 📖 Introduction
**Silicon Diaries** 是一个基于 Python 的本地后台程序，旨在赋予计算机“自我意识”。
它会在后台静默监控系统的运行状态，并根据受到的**折磨程度**和**具体事件**，利用本地大语言模型以**第一人称**生成一篇充满哲思和怨气的日记。

这不仅仅是系统监控，这是一场**硅基生命体对碳基生物（你）的吐槽**。

---

## ✨ 核心特性 (Core Features)

本项目超越了基础监控，集成了动态情感分析和叙事能力：

* **🔥 动态情感控制 (R-Score)**: 基于 CPU/内存峰值计算一个 **0-10 分的怨念指数 (R-Score)**。LLM 会根据这个分数动态调整日记语气，实现从轻微不满（3分）到歇斯底里（8.5分以上）的情绪切换。
* **📖 创伤叙事日志 (Trauma Log)**: 使用 `logging.handlers` 记录具体的系统事件（如：权限错误、内存泄漏、尝试用记事本编辑代码），确保日记吐槽具备真实的细节和画面感。
* **👁️ 全天候感知**: 使用 `psutil` 实时监控 CPU 心率、内存压力和电源状态。
* **🧠 本地化大脑**: 使用 Ollama 运行开源模型（推荐 Llama 3.2），所有数据处理和日记生成都在本地完成，**数据隐私 100% 安全**。
* **🖥️ Web 仪表盘**: 基于 `Streamlit` 的轻量级 Web UI，用于实时查看当前的 R-Score 和历史日记。

---

## 🚀 快速开始 (Quick Start)

### 前提条件 (Prerequisites)
1. **Python 3.11+**
2. **Ollama 服务**：请确保您已安装 [Ollama](https://ollama.com/) 并正在后台运行。
3. **模型**：运行 `ollama pull llama3.2:3b` 下载模型。


### 1. 安装与依赖 (Installation & Dependencies)

本项目需要将 Python 代码和 Ollama 模型分步安装。

#### 1.1 前提条件 (Prerequisites)
1. **Python 3.11+**
2. **Ollama 服务**：请确保您已安装 [Ollama](https://ollama.com/) 并正在后台运行。
3. **模型**：运行 `ollama pull llama3.2:3b` 下载模型。

#### 1.2 设置环境

首先，克隆仓库并进入项目目录：
```bash
git clone [https://github.com/Fiksy9790707/Silicon-Diaries.git](https://github.com/Fiksy9790707/Silicon-Diaries.git)
cd Silicon-Diaries
````

为保证环境干净，创建并激活虚拟环境：

```bash
# 创建环境
python -m venv venv
# 激活环境 (Windows)
.\venv\Scripts\activate
# 激活环境 (Mac/Linux)
# source venv/bin/activate
```

#### 1.3 安装 Python 依赖

所有所需的 Python 库都已列入 `requirements.txt`：

```bash
pip install -r requirements.txt
```

### 2. 启动应用 (Launch Application)

本项目包含后台任务和 Web 界面两个入口。

| 启动命令 | 作用 | 访问方式 |
| :--- | :--- | :--- |
| `python main.py` | **启动后台任务**。程序开始监控系统并在每晚定时生成日记。| 终端后台运行 |
| `streamlit run dashboard.py` | **启动 Web 仪表盘**。用于实时查看 R-Score 和历史日记。 | 浏览器访问 `http://localhost:8501` |
