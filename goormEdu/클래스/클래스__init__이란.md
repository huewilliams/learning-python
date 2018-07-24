구름Edu : 바로 실행해보면서 배우는 파이썬
====================================
## 클래스 __init__이란?
<pre>class Car:
    honk = "빵빵"
    def set_info(self, color, year):
        self.color = color
        self.year = year
    def get_info(self):
        print("color : %s, year : %d" % (self.color, self.year))
my_car = Car()
my_car.set_info("Red",2017)
my_car.get_into()

new_car = Car()
new_car.get_info()
</pre>
new_car 객체에 set_info()를 통해 색깔과 제작년도를 설정하지 않고 바로 get_info()를 부르면 오류가 발생한다.  
이처럼 get_info()를 호출하기 위해서는 반드시 color와 year 값이 존재해야 한다.  
  
클래스의 인스턴스를 생성할 때 color와 year값을 받는 방법?  
<pre>class Car:
    honk = "빵빵"
    def __init__(self, color, year):
        self.color = color
        self.year = year
        print("새로운 Car 인스턴스가 생성되었다")
    def get_info(self):
        print("color : %s, year : %d"  % (self.color, self.year))
my_car = Car("Red", 2017)
my_car.get_info() </pre>
이렇게 인스턴스 생성 초기에 변수를 지정해 주는 것을 도와주는 것이  
__init__함수이다.  
__init__함수는 초기화 메서드 혹은 생성자라고 불리며 이 함수의 인자들은 인스턴스를 만들 때 함께 선언해 주어야 한다.  
인스턴스 = 클래스(변수1, 변수2)  
  
새로운 인스턴스가 만들어 질 때 __init__ 함수가 호출된다.  
