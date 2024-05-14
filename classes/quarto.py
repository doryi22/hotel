from classes.gclass import Gclass

class Quarto(Gclass):
    obj = dict() 
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    att = ['_client_code', '_name', '_dob', '_porta', '_cod_tipo']
    des = ['Client Code', 'Name', 'Date of Birth', 'Porta', 'Cod Tipo']
    
    def __init__(self, _client_code, _name, _dob, porta, cod_tipo):
        super().__init__()
        self._client_code = _client_code 
        self._name = _name
        self._dob = _dob
        self._porta = porta 
        self._cod_tipo = cod_tipo
        Quarto.obj[_client_code] = self
        Quarto.lst.append(_client_code)

    @property
    def client_code(self):
        return self._client_code
    
    @client_code.setter
    def client_code(self, novo_code):
        self._client_code = novo_code
    
    @property
    def name(self):
        return self._name
    
    @property
    def dob(self):
        return self._dob
    
    @property
    def porta(self):
        return self._porta
    
    @property
    def cod_tipo(self):
        return self._cod_tipo
