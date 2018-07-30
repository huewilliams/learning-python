# 웹 문서 불러오기
import urllib.request

req = urllib.request
print(req.urlopen("https://github.com/huewilliams"))
# urlopen 함수의 인수에 얻고 싶은 웹 페이지의 주소를 넣어 사용한다.
# urlopen 함수는 웹에서 얻은 데이터에 대한 객체를 돌려준다.
