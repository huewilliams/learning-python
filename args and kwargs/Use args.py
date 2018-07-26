# * args 의 사용법

# 대부분 * args 와 ** kwargs 는 함수를 정의 할 때 사용됩니다.
# * args 와 ** kwargs 는 가변 갯수의 인자들을 함수에 넣어줍니다.
# 여기서 가변 갯수의 인자라 함은, 사용자들이 얼마나 많은 인자들을 함수에 넣을지 모르는, 즉 갯수가 변할 수 있는 상황에서 * args와 ** kwargs를 사용할 수 있다는 뜻입니다.
# * args 는 키워드 되지않은 가변 갯수의 인자들을 함수에 보낼 때 사용합니다.
def test_var_args(f_arg, *argv):
    print ("첫 번째 인자 : ",f_arg)
    for arg in argv:
        print("argv 의 다른 인자 : ", arg)

test_var_args('huewilliams', 'like', 'python', 'node.js')
