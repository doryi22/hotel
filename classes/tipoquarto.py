from classes.gclass import Gclass
class TipoQuarto(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ""
    auto_number = 0
    nkey = 1
    
    att = ["_cod_tipo", "_descricao", "_capacidade", "_valor"]
    
    header = "Tipo de Quarto"
    
    des = ["Código do tipo de quarto", "Descrição do tipo de quarto", "Capacidade do tipo de quarto", "Valor"]
    
    def __init__(self, cod_tipo, descricao, capacidade, valor):
        super().__init__()
        self._cod_tipo = cod_tipo
        self._descricao = descricao
        self._capacidade = capacidade
        self._valor=valor
        
        TipoQuarto.obj[cod_tipo] = self
        TipoQuarto.lst.append(cod_tipo)
        
    @property 
    def cod_tipo(self):
        return self._cod_tipo

    @property 
    def descricao(self):
        return self._descricao
    
    @property 
    def capacidade(self):
        return self._capacidade
    
    @property 
    def valor(self):
        return self._valor 