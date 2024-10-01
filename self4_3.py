import time
from datetime import datetime

for i in range(5):
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S")
    print(f"Время: {current_time}")
    time.sleep(1)