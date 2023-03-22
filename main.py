import psutil
import time
from colorama import init, Fore, Style

init() # تهيئة وحدة colorama

# بناء دالة لتحويل بايت الى مقياس مثل الكيلو بايت او الميغا بايت
def convert_bytes(bytes):
    """Convert bytes to MB or GB"""
    if bytes >= 1073741824:
        bytes = f'{bytes / 1073741824:.2f} GB'
    elif bytes >= 1048576:
        bytes = f'{bytes / 1048576:.2f} MB'
    elif bytes >= 1024:
        bytes = f'{bytes / 1024:.2f} KB'
    else:
        bytes = f'{bytes} bytes'
    return bytes

while True:
    # الحصول على معلومات استخدام الذاكرة والمعالجة المركزية
    cpu_percent = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    memory_total = psutil.virtual_memory().total
    memory_available = psutil.virtual_memory().available
    
    # تنسيق البيانات
    cpu_text = f'CPU: {cpu_percent}%'
    memory_text = f'Memory: {convert_bytes(memory_available)}/{convert_bytes(memory_total)} ({memory_usage}%)'
    
    # تنسيق النص مع التصميم modern style
    cpu_color = Fore.GREEN if cpu_percent < 50 else Fore.YELLOW if cpu_percent < 80 else Fore.RED
    memory_color = Fore.GREEN if memory_usage < 50 else Fore.YELLOW if memory_usage < 80 else Fore.RED
    cpu_text = f'{cpu_color}{Style.BRIGHT}{cpu_text:>20}{Style.RESET_ALL}'
    memory_text = f'{memory_color}{Style.BRIGHT}{memory_text:>40}{Style.RESET_ALL}'
    
    # عرض البيانات
    print(f'\r{cpu_text} {memory_text}', end='')
    time.sleep(1)
