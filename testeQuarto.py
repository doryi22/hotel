# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:14:01 2024

@author: inesr
"""

from datafile import filename

from classes.quarto import Quarto

Quarto.read(filename + 'hotel.db')

obj = Quarto.from_string("12A;standart")

print("objeto sem estar gravado ",obj)
Quarto.insert(getattr(obj,Quarto.att[0]))

obj = Quarto.from_string("13A;Suite")
Quarto.insert(getattr(obj,Quarto.att[0]))


print("\nLista dos objetos gravados " ,Quarto.lst)