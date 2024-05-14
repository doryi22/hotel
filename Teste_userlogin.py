# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:07:17 2024

@author: inesr
"""

from datafile import filename

from classes.userlogin import Userlogin

Userlogin.read(filename + 'hotel.db')

obj = Userlogin.from_string("alberto;albert@12")

print("objeto sem estar gravado ",obj)
Userlogin.insert(getattr(obj,Userlogin.att[0]))

obj = Userlogin.from_string("joao;jo@o9")
Userlogin.insert(getattr(obj,Userlogin.att[0]))


print("\nLista dos objetos gravados " ,Userlogin.lst) 