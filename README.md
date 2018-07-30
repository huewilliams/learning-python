# learning-python
this repository is made for upload .py files that I learned python

## 기본 파이썬 문법 정리 
Goorm Edu 
* 함수
* 파일 입출력
* 클래스
* 모듈 분리

## Crawling  
웹 크롤링 프로젝트는 Kaist_sonata_camp 레포지토리에 있다.

## GUI  
tkinter 프로젝트는 Kaist_sonata_camp 레포지토리에 있다.
  
## Date/Time Module  
날짜와 시간에 관련된 모듈의 예제를 정리해놓았다.  
`strftime method`  
  * 지금 현재의 날짜와 시간을 문자열로 출력  
`strptime method`    
  * 날짜, 시간형식의 문자열을 datetime으로 변환  
`replace method`    
  * 날짜나 시간을 변경    
`datetime.date`  
  * 날짜만 관리  
`datetime.time`  
  * 시간만 관리  
`datetime.datetime.combine`  
  * datetime.date 와 datetime.time을 합침    
`timetuple method`  
  * datetime의 각 날짜와 시간에 관련된 항목값에 접근  
`datetime.timedelta`  
  * 날짜, 시간 연산    
  * datetime에서 datetime을 빼면 timedelta 값을 얻을 수 있다.  
  
  
## * args and ** kwargs
### 1. * args의 사용법
대부분 * args와 ** kwargs는 함수를 정의 할 때 사용됩니다.  
\* args와 ** kwargs는 가변 갯수의 인자들을 함수에 넣어줍니다.   
여기서 가변 갯수의 인자라 함은, 사용자들이 얼마나 많은 인자들을 함수에 넣을지 모르는, 즉 갯수가 변할 수 있는 상황에서 * args와 ** kwargs를 사용할 수 있다는 뜻입니다.  
\* args는 키워드 되지않은 가변 갯수의 인자들을 함수에 보낼 때 사용합니다.  
예제 코드)  
<pre>
def test_var_args(f_arg, *argv):
    print ("첫 번째 인자:", f_arg)
    for arg in argv:
        print ("*argv의 다른 인자", arg)

test_var_args('huewilliams', 'like', 'python', 'nodeJS')
</pre>
다음과 같은 결과를 반환합니다.  
<pre>
첫번째 인자: huewilliams
*argv의 다른 인자: like
*argv의 다른 인자: python
*argv의 다른 인자: nodeJS
</pre>  
  
### 2. ** kwargs 의 사용법  
\** kwargs는 키워드된 가변 갯수의 인자들을 함수에 보낼 때 사용합니다.  
\** kwargs는 함수가 이름이 지정된 인자를 처리할 때 사용해야합니다.  
예제 코드)  
<pre>
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems(): # python3: kwargs.items()
            print "%s == %s" % (key, value) # python3: print("%s == %s" % (key, value))

>>> greet_me(name="huewilliams")
name == huewilliams   </pre>
  
### 3. 함수를 호출하기 위한 \* args와 \** kwargs
\* args와 \** kwargs를 사용해서 어떻게 함수를 호출할지 알아보겠습니다.  
<pre>
def test_args_kwargs(arg1, arg2, arg3):
        print ("인자1:", arg1)
        print ("인자2:", arg2)
        print ("인자3:", arg3)
</pre>
이제 위의 간단한 함수에게 인자를 전달하기 위해 \* args 혹은 \** kwargs를 사용할 수 있습니다.  
<pre>
# *args
>>> args = ("two", 3, 5)
>>> test_args_kwargs(*args)
인자1: two
인자2: 3
인자3: 5

# **kwargs:
>>> kwargs = {"인자3": 3, "인자2": "two", "인자1": 5} # arg(숫자)는 위 함수의 인자의 이름과 같아야합니다.
>>> test_args_kwargs(**kargs)
인자1: 5
인자2: two
인자3: 3
</pre>
\* arg, \** kwargs, 형식 인자(format args)의 사용순서  
위 3가지를 함수에서 동시에 사용하려면 아래와 같이 사용합니다.  
<pre>
some_func(fargs, *args, **kwargs)
</pre>
  
### 4. 언제 사용할까?  
일반적으로 함수의 데코레이터를 만들 때 사용합니다.    
몽키패칭을 할 때도 사용할 수 있습니다.  
몽키패칭은 런타임(실행) 중에 코드 일부를 수정한다는 것입니다.
  
  
## `URLLIB` 라이브러리  
urllib 라이브러리는 Python에서 웹과 관련된 데이터를 쉽게 이용하게 도와주는 라이브러리입니다.  
### `request` 모듈 
웹을 열어서 데이터를 읽어오는 역할
### `urlopen` : 웹 문서 불러오기  
<pre>
import urllib.request
req = urllib.request
req.urlopen("https://kimdoky.github.io")
결과 : http.client.HTTPResponse object at 0x102745358
</pre>
urlopen함수의 인수에 데이터를 얻고 싶은 웹 페이지의 주소를 넣어 사용합니다. 
urlopen함수는 웹에서 얻은 데이터에 대한 객체를 돌려줍니다.
  
### `getheaders()` : 웹 서버의 정보 받아오기  
<pre>
import urllib.request

req = urllib.request
d = req.urlopen("https://github.com/huewilliams")
status = d.getheaders()
for s in status:
    print(s)
</pre>
결과
<pre>
('Date', 'Mon, 30 Jul 2018 02:18:59 GMT')
('Content-Type', 'text/html; charset=utf-8')
('Transfer-Encoding', 'chunked')
('Connection', 'close')
('Server', 'GitHub.com')
('Status', '200 OK')
('Cache-Control', 'no-cache')
('Vary', 'X-Requested-With')
('Set-Cookie', 'has_recent_activity=1; path=/; expires=Mon, 30 Jul 2018 03:18:58 -0000')
('Set-Cookie', '_octo=GH1.1.736200713.1532917139; domain=.github.com; path=/; expires=Thu, 30 Jul 2020 02:18:59 -0000')
('Set-Cookie', 'logged_in=no; domain=.github.com; path=/; expires=Fri, 30 Jul 2038 02:18:59 -0000; secure; HttpOnly')
('Set-Cookie', '_gh_sess=STd2TERoeGQ3ZzB0ZTE1Tnd4Vnh2UGl2Z2pOU3JNZVg1ekF5QkhpNk9mcE9Oa05EZG1rY05ySjA2N1RlTlFia0doaDczK1RPaW5qTXgzdkdUNXZNTmVBbU8zWmh4SjNhNUdSTW5kZ25aNWNyUEErSUtmM2k3SEs5TkRBSG1rV1IrVlBKUlo3eVJhN0pEYVRDTnZlVmp4L28va3IxVk1HeFNqcWhaZG5jaEdYbWFEQjYyYm14N1BZVGRuWCtnTmJZNUg4NFhlMUs2KzVHbFNtc0FvN2RzQT09LS0wNkVRRlNuUUtoNlZnWWFQemFab2Z3PT0%3D--b05f12638b71dcb9bc60b300270f0317f7fc19b9; path=/; secure; HttpOnly')
('X-Request-Id', 'b1fae8c0-2cb1-48b2-94ff-80a9fa55639e')
('X-Runtime', '0.353048')
('Strict-Transport-Security', 'max-age=31536000; includeSubdomains; preload')
('X-Frame-Options', 'deny')
('X-Content-Type-Options', 'nosniff')
('X-XSS-Protection', '1; mode=block')
('Referrer-Policy', 'origin-when-cross-origin, strict-origin-when-cross-origin')
('Expect-CT', 'max-age=2592000, report-uri="https://api.github.com/_private/browser/errors"')
('Content-Security-Policy', "default-src 'none'; base-uri 'self'; block-all-mixed-content; connect-src 'self' uploads.github.com status.github.com collector.githubapp.com api.github.com www.google-analytics.com github-cloud.s3.amazonaws.com github-production-repository-file-5c1aeb.s3.amazonaws.com github-production-upload-manifest-file-7fdce7.s3.amazonaws.com github-production-user-asset-6210df.s3.amazonaws.com wss://live.github.com; font-src assets-cdn.github.com; form-action 'self' github.com gist.github.com; frame-ancestors 'none'; frame-src render.githubusercontent.com; img-src 'self' data: assets-cdn.github.com identicons.github.com collector.githubapp.com github-cloud.s3.amazonaws.com *.githubusercontent.com; manifest-src 'self'; media-src 'none'; script-src assets-cdn.github.com; style-src 'unsafe-inline' assets-cdn.github.com")
('X-Runtime-rack', '0.360164')
('Vary', 'Accept-Encoding')
('X-GitHub-Request-Id', '692B:49E3:4051A5C:639D631:5B5E7592')
</pre>
getheaders() 함수를 사용하면 서버에 대한 정보를 리스트로 돌려줍니다.  
리스트를 출력해보면 운영체제나 날짜, 타입 등 여러 가지 정보를 알 수 있습니다.   
이 정보들은 크롤링하려는 홈페이지가 어떤 형식으로 만들어 졌는지 알 수 있습니다.  
  
### `status` : 웹 페이지의 상태 확인하기  
<pre>
import urllib.request
req = urllib.request
d = req.urlopen("https://github.com/huewilliams")
print(d.status)
</pre>
웹 서버의 상태를 확인할 수 있습니다. 200 : OK  
 
