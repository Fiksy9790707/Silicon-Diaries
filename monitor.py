# monitor.py
import psutil
import datetime
import memory  # <--- 导入刚才写的 memory 模块


def get_vital_signs():
    print("🏥 正在自检生命体征...")

    cpu_usage = psutil.cpu_percent(interval=1)

    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)
    now = datetime.datetime.now()
    uptime = now - boot_time
    uptime_str = str(uptime).split('.')[0]

    battery = psutil.sensors_battery()
    battery_info = "电源供电"
    if battery:
        status = "充电中" if battery.power_plugged else "放电中"
        battery_info = f"{battery.percent}% ({status})"

    print("-" * 30)
    print(f"🧠 CPU 负载:   {cpu_usage}%")
    print(f"📦 内存占用:   {memory_usage}%")
    print("-" * 30)

    return {
        "cpu": cpu_usage,
        "memory": memory_usage,
        "uptime_str": uptime_str,
        "battery": battery_info
    }


if __name__ == "__main__":
    # 1. 获取数据
    stats = get_vital_signs()

    # 2. 存入记忆 (Phase 2 新增功能)
    print("🧠 正在写入海马体...")
    memory.update_memory(stats)