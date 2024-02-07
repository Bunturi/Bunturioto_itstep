
from datetime import datetime

while True:
    time_now = datetime.now()
    frmt = time_now.strftime("%H:%M:%S")
    print(f"\rCurrent Time: {frmt}", end="")
