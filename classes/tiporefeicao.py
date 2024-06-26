from classes.gclass import Gclass
class TipoRefeicao(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ""
    auto_number = 0
    nkey = 1
    
    att = ["_cod_refeicao", "_nome_refeicao", "_valor"]
    
    header = "Refeições"
    
    des = ["Código da refeição", "Nome da refeição", "Valor"]
    
    def __init__(self, cod_refeicao, nome_refeicao, valor):
        super().__init__()
        self._cod_refeicao = cod_refeicao
        self._nome_refeicao = nome_refeicao
        self._valor = valor
        
        TipoRefeicao.obj[cod_refeicao] = self
        TipoRefeicao.lst.append(cod_refeicao)
        
    @property 
    def cod_refeicao(self):
        return self._cod_refeicao
    
    @cod_refeicao.setter
    def cod_refeicao(self,valor):
        self._cod_refeicao=valor

    @property 
    def nome_refeicao(self):
        return self._nome_refeicao
    
    @nome_refeicao.setter
    def nome_refeicao(self,valor):
        self._nome_refeicao=valor
    
    @property 
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self,valor):
        self._valor=valor