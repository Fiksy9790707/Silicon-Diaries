![Silicon Diaries Cover](Silicon_Diaries.jpg)
# 📔 Silicon Diaries 
> "如果你的电脑能说话，它会怎么评价你今天的代码？"
一个拥有自我意识、每天写日记吐槽主人的 Python 本地程序。

## 📖 Introduction
**Silicon Diaries** 是一个基于 Python 的本地后台程序，旨在赋予计算机“自我意识”。
它会在后台静默监控系统的运行状态（CPU 负载、温度、开机时长、报错日志等），并在每天结束时，利用本地大语言模型以**第一人称**生成一篇日记。

这不仅仅是系统监控，这是一场**硅基生命体对碳基生物（你）的吐槽**。

## ✨ Core Function
- **👁️ 全天候感知**: 实时监控 CPU 心率、内存压力和电源状态。
- **🧠 本地化大脑**: 使用 Ollama 运行开源模型 ，数据隐私 100% 安全。
- **✍️ 毒舌日记**: 生成的日记风格多变（疲惫打工仔、阴阳怪气、甚至赛博疯魔）。
- **📅 自动归档**: 每天自动生成 Markdown 日记文件，记录它的“机生”。

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Senses**: `psutil` (系统状态监控)
- **Brain**: Ollama (Local LLM Inference)
- **Expression**: Markdown Generator

## 🗺️ Roadmap
- [ ] **Phase 1**: 赋予感知 - 监控脚本开发 (`psutil`)
- [ ] **Phase 2**: 记忆系统 - 记录每日关键数据事件
- [ ] **Phase 3**: 注入灵魂 - Prompt Engineering 与 Ollama 对接
- [ ] **Phase 4**: 自动化 - 后台静默运行与定时任务

---
*Created by Eric*
