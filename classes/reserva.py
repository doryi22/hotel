from tipoquarto import TipoQuarto
from tiporefeicao import TipoRefeicao
from classes.gclass import Gclass
import datetime

class Reserva(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    att = ['_cod_reserva', '_data_inicio', '_data_fim', '_cod_refeicao', '_client_code','_cod_tipo','_opiniao', '_user', '_npessoas', '_valor_final']
    header = 'Reserva'
    des = ['Código de reserva', 'Data inicio', 'Data fim', 'Código de refeição', 'Código do Cliente','Código TipoQuarto', 'Opiniao', 'User', 'Número de pessoas', 'Valor da Estadia']

    def __init__(self, cod_reserva, data_inicio, data_fim, cod_refeicao, client_code, cod_tipo=None, opiniao='', user='', npessoas=0, valor_final=0):
        super().__init__()
        if cod_tipo and cod_tipo in TipoQuarto.obj:
            tipo = TipoQuarto.obj[cod_tipo]
            if npessoas > tipo.capacidade:
            	raise ValueError (f"Nº pessoas maior que a capacidade do quarto")
            else:
                self._npessoas = npessoas
        else:
            self._npessoas=npessoas
            
        self._cod_reserva=cod_reserva
        self._data_inicio=data_inicio
        self._data_fim=data_fim
        self._cod_refeicao=cod_refeicao
        self._client_code=client_code
        self._cod_tipo = cod_tipo
        self._opiniao=opiniao
        self._user=user
        self._valor_final=valor_final
        Reserva.obj[cod_reserva] = self
        Reserva.lst.append(cod_reserva)

        
    @property
    def cod_reserva(self):
        return self._cod_reserva
    
    @property 
    def data_inicio(self):
        self._data_inicio = datetime.date.fromisoformat(self._data_inicio)
        return self._data_inicio
    
    @property 
    def data_fim(self):
        self._data_fim = datetime.date.fromisoformat(self._data_fim)
        return self._data_fim
    
    @property 
    def opiniao(self):
        return self._opiniao 
    
    @opiniao.setter 
    def opiniao(self, comentario):
        self._opiniao=comentario
        
    
    @property 
    def valor_final(self):
        data_inicio_date = datetime.date.fromisoformat(self.data_inicio)
        data_fim_date = datetime.date.fromisoformat(self.data_fim)
        num_days = (data_fim_date - data_inicio_date).days
        tipo_quarto = TipoQuarto.obj[self._cod_tipo]
        tipo_refeicao = TipoRefeicao.obj[self._cod_refeicao]
        valor_final = num_days * (tipo_quarto.valor + self._npessoas*tipo_refeicao.valor)
        return valor_final
       


        