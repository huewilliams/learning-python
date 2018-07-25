# 날짜, 시간형식의 문자열을 datetime으로 만들려면 strptime메서드를 사용하면 된다.
import datetime

myDatetimeStr = '2018-07-25 12:32:15'
# 날짜 시간 형식의 문자열을 생성
myDatetime = datetime.datetime.strptime(myDatetimeStr, '%Y-%m-%d %H:%M:%S')
# strptime 메서드로 문자열을 datatime 으로 변환
print(type(myDatetime))
# 출력결과 : <class 'datetime.datetime'>
print(myDatetime)