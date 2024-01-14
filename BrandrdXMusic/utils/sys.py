import time

import psutil

from BrandrdXMusic.misc import _boot_
from BrandrdXMusic.utils.formatters import get_readable_time


async def bot_sys_stats():
     itne_time_sa_gaga_hua_hu = int(time.time() - _boot_)
    itne_time_sa_nahi_soya = f"{get_readable_time(bot_uptime)}"
    CPU = f"{psutil.cpu_percent(interval=0.5)}%"
    RAM = f"{psutil.virtual_memory().percent}%"
    DISK = f"{psutil.disk_usage('/').percent}%"
    return UP, CPU, RAM, DISK
