# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (não tem acesso ao self nem cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        cls.user = user
        cls.password = password
        return cls
    
    @staticmethod
    def soma(x, y):
        return x + y

# c1 = Connection()
c1 = Connection.create_with_auth('luiz', '1234')
# c1.set_user('luiz')
# c1.set_password('123')
print(Connection.soma(2, 3))
print(c1.user)
print(c1.password)