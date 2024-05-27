from datafile import filename

from classes.tipoquarto import TipoQuarto

TipoQuarto.read(filename + 'hotel.db')

obj = TipoQuarto.from_string("1;elegante;1;400;quarto_elegante.jpg")
TipoQuarto.insert(getattr(obj,TipoQuarto.att[0]))
obj = TipoQuarto.from_string("2;diamante;2;1000;diamante.jpg")
TipoQuarto.insert(getattr(obj,TipoQuarto.att[0]))
obj = TipoQuarto.from_string("3;cidade chique;2;500;cidade_chique.jpg")
TipoQuarto.insert(getattr(obj,TipoQuarto.att[0]))
obj = TipoQuarto.from_string("4;classico;3;750;classico.jpg")
TipoQuarto.insert(getattr(obj,TipoQuarto.att[0]))

# obj = TipoQuarto.from_string("a007;2024-08-01;2024-08-08;123;cd123;2")
# TipoQuarto.insert(getattr(obj,TipoQuarto.att[0]))


print("\nLista dos objetos gravados " ,TipoQuarto.lst)

