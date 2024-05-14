# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:04:07 2024

@author: inesr
"""

from datafile import filename

from classes.cliente import Cliente

Cliente.read(filename + 'hotel.db')

obj = Cliente.from_string("ab123;alberto;4;1999-05-23")

print("objeto sem estar gravado ",obj)

Cliente.insert(getattr(obj,Cliente.att[0]))

obj = Cliente.from_string("cd123;maria;3;1999-08-02")
Cliente.insert(getattr(obj,Cliente.att[0]))


print("\nLista dos objetos gravados " ,Cliente.lst)