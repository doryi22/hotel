# -*- coding: utf-8 -*-


from datafile import filename

from classes.reserva import Reserva

Reserva.read(filename + 'hotel.db')

obj = Reserva.from_string("a006;2024-07-01;2024-07-08;456;ab123;5;;;2")

print("objeto sem estar gravado ",obj)

Reserva.insert(getattr(obj,Reserva.att[0]))

obj = Reserva.from_string("a007;2024-08-01;2024-08-08;123;cd123;6;;;1")
Reserva.insert(getattr(obj,Reserva.att[0]))


print("\nLista dos objetos gravados " ,Reserva.lst)

