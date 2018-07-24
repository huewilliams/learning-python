class Customer:
    welcome = "반갑습니다"
    def info(self, id):
        print("사용자의 아이디 : "+id)
Customer = Customer()
print(Customer.welcome)
print(Customer.info('huewilliams'))