# datetime 에서 datetime 을 빼면 timedelta 값을 얻을 수 있다.
import datetime

oneDatetime = datetime.datetime.strptime('2018-07-26 00:00:00', '%Y-%m-%d %H:%M:%S')
twoDatetime = datetime.datetime.strptime('2018-07-27 00:00:10', '%Y-%m-%d %H:%M:%S')
result = twoDatetime - oneDatetime
print(result)
# 1day , 0:00:10
print(result.days)
# 1
print(result.seconds)
# 10
