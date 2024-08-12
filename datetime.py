import datetime

now = datetime.datetime.now()
local_now = now.astimezone()
local_tz = local_now.tzinfo
local_tzname = local_tz.tzname(local_now)
offset = local_tz.utcoffset(None).seconds
print(offset)
print(local_tzname)