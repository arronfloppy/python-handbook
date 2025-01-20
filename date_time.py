import time
from datetime import date, datetime, timedelta, timezone

time1 = time.time()
print(str(time1))


print(str(datetime.now(timezone.utc)))
dt1 = datetime.fromisoformat('2024-08-14 18:10:23+02:00')
dt2 = datetime.now(timezone.utc)

print(str(dt2-dt1))
print(str(dt2-5))
