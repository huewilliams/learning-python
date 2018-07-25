import datetime

# 날짜만을 관리하기 위해서는 datetime.date() 를 사용
d = datetime.date(2018, 7, 25)
print(d)
# 시간만을 관리하기 위해서는 datetime.time() 을 사용
t = datetime.time(8, 30, 15)
print(t)
# datetime.date 와 datetime.time 을 합칠려면 datetime.datetime.combine() 을 사용
dt = datetime.datetime.combine(d, t)
print(dt)