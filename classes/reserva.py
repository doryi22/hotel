# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:16:04 2024

@author: inesr
"""

from classes.Gclass import Gclass
from tiporefeicao import TipoRefeicao

class Reserva(Gclass):
    obj=dict()
    lst=list()
    pos=0
    sortkey=''
    auto_number = 0
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code_reservation']
    def _init__(self, code_reservation):
        super()._init_()
        self._code_reservation=str(code_reservation)
        
    @property 
    def code_reservation(self):
        return self._code_reservation
    