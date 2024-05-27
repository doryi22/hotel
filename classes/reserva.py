from classes.tipoquarto import TipoQuarto
from classes.tiporefeicao import TipoRefeicao
from classes.gclass import Gclass
import datetime
from datafile import filename
TipoQuarto.read(filename + 'hotel.db')
TipoRefeicao.read(filename + 'hotel.db')

class Reserva(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    att = ['_cod_reserva', '_data_inicio', '_data_fim', '_cod_refeicao', '_client_code','_cod_tipo','_opiniao', '_user', '_npessoas', '_valor_final']
    header = 'Reserva'
    des = ['Código de reserva', 'Data inicio', 'Data fim', 'Código de refeição', 'Código do Cliente','Código TipoQuarto', 'Opiniao', 'User', 'Número de pessoas', 'Valor da Estadia']

    def __init__(self, cod_reserva, data_inicio, data_fim, cod_refeicao, client_code, cod_tipo, opiniao='', user='', npessoas=0, valor_final=0):
        super().__init__()
        if cod_tipo in TipoQuarto.obj:
            tipo = TipoQuarto.obj[cod_tipo]
        if npessoas == 0:
            self._npessoas = int(tipo.capacidade)
        if int(npessoas) > int(tipo.capacidade):
            raise ValueError (f"Nº pessoas maior que a capacidade do quarto")
        else:
            self._npessoas = int(npessoas)
            
        self._cod_reserva=cod_reserva
        self._data_inicio=data_inicio
        self._data_fim=data_fim
        self._cod_refeicao=cod_refeicao
        self._client_code=client_code
        self._cod_tipo = cod_tipo
        self._opiniao=opiniao
        self._user=user
        self._valor_final = self.calculate_valor_final() if valor_final == 0 else valor_final
        Reserva.obj[cod_reserva] = self
        Reserva.lst.append(cod_reserva)

    def calculate_valor_final(self):
        data_inicio_date = datetime.date.fromisoformat(self._data_inicio)
        data_fim_date = datetime.date.fromisoformat(self._data_fim)
        num_days = (data_fim_date - data_inicio_date).days
        tipo_quarto = TipoQuarto.obj[self._cod_tipo]
        tipo_refeicao = TipoRefeicao.obj[self._cod_refeicao]
        valor_quarto = float(tipo_quarto.valor)
        valor_refeicao = float(tipo_refeicao.valor)
        npessoas = float(self._npessoas)
        valor_final = num_days * (valor_quarto + npessoas * valor_refeicao)
        return valor_final

        
    @property 
    def cod_reserva(self):
        return self._cod_reserva
    
    @cod_reserva.setter 
    def cod_reserva(self,valor):
        self._cod_reserva=valor
    
    @property 
    def data_inicio(self):
        self._data_inicio = datetime.date.fromisoformat(self._data_inicio)
        return self._data_inicio
    
    @data_inicio.setter 
    def data_inicio(self,data):
        self._data_inicio = datetime.date.fromisoformat(data)
        
    @property 
    def data_fim(self):
        self._data_fim = datetime.date.fromisoformat(self._data_fim)
        return self._data_fim
    
    @data_fim.setter 
    def data_fim(self,data):
        self._data_fim = datetime.date.fromisoformat(data)
    
    @property 
    def opiniao(self):
        return self._opiniao 
    
    @opiniao.setter 
    def opiniao(self, comentario):
        self._opiniao=comentario
        
    @property 
    def valor_final(self):
        return self._valor_final
