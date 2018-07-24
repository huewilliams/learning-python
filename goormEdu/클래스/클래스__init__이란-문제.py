class Member:
    def __init__(self, id, password):
        self.id = id
        self.password = password
        print('초기 설정이 완료되었습니다.')

    def getId(self):
        print("사용자 아이디 : %s , 사용자 비밀번호 : %s" %(self.id, self.password))
VVIP = Member('huewilliams','0123')
VVIP.getId()