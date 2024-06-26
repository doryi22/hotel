from classes.gclass import Gclass
# from classes.tipoquarto import TipoQuarto

class Quarto(Gclass):
    obj = dict() 
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    att = ['_porta', '_cod_tipo']
    header = 'Quarto'
    des = ['Porta', 'Cod Tipo']
    
    def __init__(self, porta, cod_tipo):
        super().__init__()
        self._porta = porta 
        self._cod_tipo = cod_tipo
        Quarto.obj[porta] = self
        Quarto.lst.append(porta)
    
    @property
    def porta(self):
        return self._porta
    
    @porta.setter 
    def porta(self,valor):
        self._porta=valor 
        
    @property
    def cod_tipo(self):
        return self._cod_tipo
    
    @cod_tipo.setter 
    def cod_tipo(self,valor):
        self._cod_tipo=valor