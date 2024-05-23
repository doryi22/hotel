from classes.gclass import Gclass
import datetime

class Cliente(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    att = ['_client_code','_name', '_dob']
    header = 'Cliente'
    des = ['Client Code','Name','Date of Birth']

    def __init__(self, client_code, name, dob):
        super().__init__()
        self._client_code = client_code
        self._name = name
        self._dob = dob
        self._idade = self.idade
        Cliente.obj[client_code] = self
        Cliente.lst.append(client_code)
        
    @property
    def client_code(self):
        return self._client_code
    
    @property
    def name(self):
        return self._name
    
    @property
    def dob(self):
        dob = datetime.date.fromisoformat(self._dob)
        self._dob = dob
        return self._dob
    
    @property
    def idade(self):
        tday = datetime.date.today()
        age = tday.year - self.dob.year
        if tday.month < self.dob.month or \
            (tday.month == self.dob.month and tday.day < self.dob.day):
            age -= 1
        return age 