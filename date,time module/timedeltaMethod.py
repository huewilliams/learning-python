import datetime

now = datetime.datetime.now()
print(now)

tommorrow = now + datetime.timedelta(days=1)
# timedelta 를 이용하여 datetime 에 하루(1 day)를 더할 수 있다.
print(tommorrow)
# timedelta에 들어갈 수 있는 인자값은 아래와 같다.
# – 1주 : datetime.timedelta(weeks=1)
# – 1일 : datetime.timedelta(days=1)
# – 1시간 : datetime.timedelta(hours=1)
# – 1분 : datetime.timedelta(minutes=1)
# – 1초 : datetime.timedelta(seconds=1)
# – 1밀리초 : datetime.timedelta(milliseconds=1)
# – 1마이크로초 : datetime.timedelta(microseconds=1)
