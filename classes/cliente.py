from classes.gclass import Gclass
import datetime

class Cliente(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    att = ['_client_code','_name', '_dob']
    des = ['Client Code','Name','Date of Birth']

    def __init__(self, client_code, name, npessoas):
        super().init()
        self._client_code = client_code
        self._name = name
        self._dob = None
        self._idade = None
        self._npessoas = npessoas
        Cliente.obj[client_code] = self
        Cliente.lst.append(client_code)
        
    @property
    def client_code(self):
        return self._client_code
    
    @property
    def name(self):
        return self._name
    
    @property
    def dob(self, dob):
        self._dob = datetime.date.fromisoformat(dob)
        return self._dob
    
    @property
    def idades(self):
        tday = datetime.date.today()
        age = tday.year - self.dob.year
        if tday.month < self.dob.month or \
            (tday.month == self.dob.month and tday.day < self.dob.day):
            age -= 1
            self._idades = age 

    
