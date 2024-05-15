# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:00:44 2024

@author: inesr
"""

from datafile import filename

from classes.tiporefeicao import TipoRefeicao

TipoRefeicao.read(filename + 'hotel.db')

obj = TipoRefeicao.from_string("123;almoco;20")

print("objeto sem estar gravado ",obj)
TipoRefeicao.insert(getattr(obj,TipoRefeicao.att[0]))

obj = TipoRefeicao.from_string("456;jantar;60")
TipoRefeicao.insert(getattr(obj,TipoRefeicao.att[0]))


print("\nLista dos objetos gravados " ,TipoRefeicao.lst)