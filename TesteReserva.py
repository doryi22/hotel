# -*- coding: utf-8 -*-


from datafile import filename

from classes.reserva import Reserva

Reserva.read(filename + 'hotel.db')


obj = Reserva.from_string("a000;2024-07-03;2024-07-18;123;1;4;;root;3")
Reserva.insert(getattr(obj,Reserva.att[0]))
obj = Reserva.from_string("a001;2024-09-17;2024-09-26;789;2;5;;root;4")
Reserva.insert(getattr(obj,Reserva.att[0]))
obj = Reserva.from_string("a002;2024-04-20;2024-04-22;456;3;3;Comida muito boa, staff muito prestavel e acolhedora. É uma pena não ter fichas junto da cama, mas assim livro-me das radiações.;root;2")
Reserva.insert(getattr(obj,Reserva.att[0]))
obj = Reserva.from_string("a003;2024-01-01;2024-01-08;456;4;1;Bom para um retiro espiritual. Nada a apontar, recomendo vivamente o atendimento professional e atencioso do staff, destacando Thiago Sobral.;root;1")
Reserva.insert(getattr(obj,Reserva.att[0]))
obj = Reserva.from_string("a004;2024-03-25;2024-03-29;456;5;2;Saliento as condições impecáveis das instalações que fui sujeito. Em termos de privacidade, no entanto, considero que devia haver seleção de hóspedes para o nível do hotel.;root;2")
Reserva.insert(getattr(obj,Reserva.att[0]))
obj = Reserva.from_string("a005;2024-07-01;2024-07-08;123;1;4;;root;2")
Reserva.insert(getattr(obj,Reserva.att[0]))

print("\nLista dos objetos gravados " ,Reserva.lst)

