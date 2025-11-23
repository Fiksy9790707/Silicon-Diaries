import time
import datetime
import schedule  # 需要安装这个库
import monitor
import diary

# --- 配置区域 ---
CHECK_INTERVAL = 60  # 每隔多少分钟检测一次身体状况
DIARY_TIME = "23:35"  # 每天几点写日记 (24小时制)


def job_monitor():
    """定期体检任务"""
    print(f"\n[潜意识] {datetime.datetime.now().strftime('%H:%M')} -> 正在悄悄检测身体状况...")
    monitor.get_vital_signs()
    # 注意：monitor.get_vital_signs 内部已经调用了 memory.update_memory
    # 所以只要运行它，数据就会自动保存到 json


def job_write_diary():
    """写日记任务"""
    print(f"\n[潜意识] {datetime.datetime.now().strftime('%H:%M')} -> 夜深了，准备开始吐槽...")
    diary.generate_diary()


def start_life():
    print("🤖 Silicon Diaries (硅基日记) 已启动...")
    print(f"   - 监测频率: 每 {CHECK_INTERVAL} 分钟")
    print(f"   - 写作时间: 每天 {DIARY_TIME}")
    print("   (程序将在后台静默运行，请不要关闭窗口...)")

    job_monitor()
    schedule.every(CHECK_INTERVAL).minutes.do(job_monitor)

    schedule.every().day.at(DIARY_TIME).do(job_write_diary)

    #死循环，保持程序一直运行
    while True:
        schedule.run_pending()
        time.sleep(1) 


if __name__ == "__main__":
    start_life()
