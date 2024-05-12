# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:38:36 2024

@author: maria
"""

import bcrypt
from classes.gclass import Gclass

class Userlogin(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    att = ['_name', '_password']
    header = 'Staff'
    des = ['Name','Password']
    username = ''

    def __init__(self, name, password):
        super()._init_()
        self._name = name
        self._password = password
        Userlogin.obj[name] = self
        Userlogin.lst.append(name)

    @property
    def name(self):
        return self._name
    
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
    

        
        
        