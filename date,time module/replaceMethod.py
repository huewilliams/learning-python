# 날짜나 시간을 변경할 때는 replace 메소드를 사용한다.
import datetime

myDatetime = datetime.datetime.strptime('2018-7-25 1:25:15', '%Y-%m-%d %H:%M:%S')
print(myDatetime)
# 2018-7-25 1:25:15

dayDatetime = myDatetime.replace(day=30)
# 날짜를 30일로 변경

# .replace(year = number) : 년도 변경
# .replace(month = number) : 월 변경
# .replace(day = number) : 일 변경

# .replace(hour = number) : 시간 변경
# .replace(minute = number) : 분 변경
# .replace(second = number) : 초 변경
# .replace(microsecond = number) : 마이크로초 변경
print(myDatetime)
print(dayDatetime)


