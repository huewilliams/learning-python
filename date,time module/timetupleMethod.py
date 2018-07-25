import datetime

now = datetime.datetime.now()
# 현재 시간
nowTuple = now.timetuple()
print(nowTuple)
# time.struct_time(tm_year = number, tm_mon = number, tm_mday = number, tm_hour = number, tm_min = number,
#                  tm_sec = number, tm_wday = number , tm_yday = number, tm_isdst = number)
print(nowTuple.tm_year)