import time
import datetime
import schedule  # 需要安装这个库
import monitor
import diary
import logging.handlers

# --- 配置区域 ---
CHECK_INTERVAL = 60  # 每隔多少分钟检测一次身体状况
DIARY_TIME = "23:35"  # 每天几点写日记 (24小时制)
TRAUMA_LOG_FILE = "trauma.log"
MAX_BYTES = 1024 * 1024


def setup_trauma_logger():
    """设置日志记录器，限制日志文件大小"""
    logger = logging.getLogger('TraumaLogger')
    logger.setLevel(logging.INFO)  # 记录 INFO 及以上级别的消息

    # 使用 RotatingFileHandler 实现日志轮换
    handler = logging.handlers.RotatingFileHandler(
        TRAUMA_LOG_FILE,
        maxBytes=MAX_BYTES,
        backupCount=1,
        encoding='utf-8'
    )
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)

    # 避免重复添加 handler
    if not logger.handlers:
        logger.addHandler(handler)
    return logger


# 全局变量：初始化日志记录器
TRAUMA_LOGGER = setup_trauma_logger()

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

    # 1. 马上先测一次，确保存活
    job_monitor()

    TRAUMA_LOGGER.warning("人类在 09:15 AM 尝试用记事本编辑 Python 代码，导致格式错误。")
    TRAUMA_LOGGER.error("发现一处内存泄漏，疑似主人使用了递归但未设退出条件。")
    TRAUMA_LOGGER.info("浏览器打开了 80 个标签页，其中 78 个是无用的购物网站。")
    # 2. 设置定时任务
    # 每隔 X 分钟测一次
    schedule.every(CHECK_INTERVAL).minutes.do(job_monitor)

    # 每天固定时间写日记
    schedule.every().day.at(DIARY_TIME).do(job_write_diary)

    # 3. 死循环，保持程序一直运行
    while True:
        schedule.run_pending()
        time.sleep(1)  # 每秒醒来检查一下有没有任务到期


if __name__ == "__main__":
    start_life()