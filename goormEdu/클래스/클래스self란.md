구름Edu : 바로 실행해보면서 배우는 파이썬
====================================
## 클래스 self란?  
<pre>class Car:
    honk = "빵빵"
    def info(self, color, year):
        print("color : %s , year : %s" % (color, year))</pre>
위와 같이 클래스의 함수의 첫 번째 인수로 self를 써 줘야만 해당 함수를 인스턴스의 함수로 사용할 수 있다.  
self는 이 함수를 부르는 객체가 해당 클래스의 인스턴스인지 확인해 주기위한 장치이다.  
self는 단순히 확인하는 것에서 나아가 객체 내의 정보를 저장하거나 불러 올 수 있다.  
<pre>calss Car:
    honk = "빵빵"
    def set_info(self, color, year):
        self.color = color
        self.year = year
    def get_info(self):
        print("color : %s, year : %s" % (self.color, self.year))
my_car = Car()
my_car.set_info("Red", 2017)
my_car.get_info() </pre>
위에서 my_car 이라는 Car의 인스턴스를 이용하여 my_car.set_info("Red",2017)를 수행하면   
self.color 에는 "Red"값이,  
self.year 에는 2017 값이 저장된다.  
이 때 self는 my_car 이라는 객체이다.  
my_car 객체를 이용하여 get_info() 함수를 호출하면 위에서 설정한 self.color과 self.year 이 출력되는 것을 볼 수 있다.  
  
즉, get_info()라는 함수는 self를 통해서 my_car 에 해당하는 color와 year을 리턴한다.
