# ** kwargs 의 사용법

# ** kwargs 는 키워드된 가변 갯수의 인자들을 함수에 보낼 때 사용합니다.
# ** kwargs 는 함수가 이름이 지정된 인자를 처리할 때 사용해야합니다.
def greet_me(** kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" % (key,value))