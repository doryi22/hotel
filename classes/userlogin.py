import bcrypt
from classes.gclass import Gclass

class Userlogin(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    att = ['_user', '_password']
    header = 'Staff'
    des = ['User','Password']
    username = ''

    def __init__(self, user, password):
        super().__init__()
        self._user = user
        self._password = password
        Userlogin.obj[user] = self
        Userlogin.lst.append(user)

    @property
    def user(self):
        return self._user
    
    @property
    def password(self):
        return ""
    
    @password.setter
    def password(self, password):
        self._password = password

    @classmethod
    def chk_password(self, user, password):
        if user in Userlogin.obj:
            obj = Userlogin.obj[user]
            valid = bcrypt.checkpw(password.encode(), obj._password.encode())
            message = "Valid"
            if not valid:
                message = 'Wrong password'
        else:
            message = 'No existent user'
        return message
    
    @classmethod
    def set_password(self, password):
        passencrypted = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return passencrypted.decode()
    

        
        
        