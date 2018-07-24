class Member:
    def setID(self, id, password):
        self.id = id
        self.password = password

    def getID(self):
        print('id : %s, password : %s' % (self.id, self.password))

user1 = Member()
user1.setID('huewilliams','0123')
user1.getID()

user2 = Member()
user2.setID('peter','5555')
user2.getID()
