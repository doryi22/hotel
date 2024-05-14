# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:16:04 2024

@author: inesr
"""

from classes.gclass import Gclass
import datetime

class Reserva(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    att = ['_cod_reserva', '_data_inicio', '_data_fim', '_cod_refeicao', '_client_code','_opiniao', '_user']
    des = ['Código de reserva', 'Data inicio', 'Data fim', 'Código de refeição', 'Código do Cliente', 'Opiniao', 'User']

    def __init__(self, cod_reserva, data_inicio, data_fim, cod_refeicao, client_code, opiniao='', user=''):
        super().init()
        self._cod_reserva=cod_reserva
        self._data_inicio=data_inicio
        self._data_fim=data_fim
        self._cod_refeicao=cod_refeicao
        self._client_code=client_code
        self._opiniao=opiniao
        self._user=user
        
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
        