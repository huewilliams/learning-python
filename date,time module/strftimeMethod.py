# 지금 현재의 날짜와 시간을 문자열로 출력하려면 strftime 메서드를 사용하면 된다.
import datetime

now = datetime.datetime.now()
# 년도-월-일 시간 : 분 : 초.밀리초
print(now)

nowDate = now.strftime('%Y-%m-%d')
# Y : year , m : month, d : day
print(nowDate)

nowTime = now.strftime('%H:%M:%S')
# H : hour, M : minute, S : second
print(nowTime)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
#  년도-월-일 시간 : 분 : 초
print(nowDatetime)
