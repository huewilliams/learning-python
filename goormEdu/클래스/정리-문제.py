class phoneBook(object):

    def __init__(self, name, number, religion, photo):
        self.name = name
        self.number = number
        self.religion = religion
        self.photo = photo
        print("info is saved")

    def showData(self):
        print("사용자 정보 조회")
        print("이름 : %s, 번호 : %s, 지역 : %s, 사진 : %s" %(self.name, self.number, self.religion, self.photo))

    def delete(self):
        print("%s의 정보를 삭제하였습니다." %(self.name))


class BestFriend(phoneBook):
    age = 17
    gender = 'man'

    def info(self):
        print('가장 친한 친구의 이름은 %s, 나이는 %s, 성별은 %s, 번호는 %s'%(self.name, self.age, self.gender, self.number))

user = BestFriend('huewilliams', '01088757506' , 'busan', 'boracay')
user.info()