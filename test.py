# Dict = {[1,2]:'a'}

class A:
    password_hash = ''
    @property
    def password(self):
        raise AttributeError

    @password.setter
    def password(self,password):
        self.password_hash = '加密后的密码'+password
    __a = 'a'


# _A__a
a = A()

a.password = '123456'
print(a.password_hash)