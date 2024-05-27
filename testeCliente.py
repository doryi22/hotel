# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:04:07 2024

@author: inesr
"""

from datafile import filename

from classes.cliente import Cliente

Cliente.read(filename + 'hotel.db')

obj = Cliente.from_string("1;Ines;2005-09-01")

print("objeto sem estar gravado ",obj)

Cliente.insert(getattr(obj,Cliente.att[0]))

obj = Cliente.from_string("2;Mariana;2003-09-12")
Cliente.insert(getattr(obj,Cliente.att[0]))

obj = Cliente.from_string("3;Oriana;2005-07-22")
Cliente.insert(getattr(obj,Cliente.att[0]))

obj = Cliente.from_string("4;Leonor;2005-09-08")
Cliente.insert(getattr(obj,Cliente.att[0]))

obj = Cliente.from_string("5;Alberto;2007-09-12")
Cliente.insert(getattr(obj,Cliente.att[0]))

obj = Cliente.from_string("7;Miguel;2005-08-12")
Cliente.insert(getattr(obj,Cliente.att[0]))


print("\nLista dos objetos gravados " ,Cliente.lst)

