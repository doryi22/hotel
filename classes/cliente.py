from classes.gclass import Gclass
import datetime

class Cliente(Gclass):

    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    att = ['_client_code','_name', '_dob', '_idade']
    header = 'Cliente'
    des = ['Client Code','Name','Date of Birth','Idade']

    def __init__(self, client_code, name, dob, idade=None):
        super().__init__()
        self._client_code = client_code
        self._name = name
        self._dob = dob
        self._idade = idade if idade is not None else self.calculate_age(dob)
        Cliente.obj[client_code] = self
        Cliente.lst.append(client_code)


    def calculate_age(self, dob):
        dob_date = datetime.date.fromisoformat(dob)
        today = datetime.date.today()
        age = today.year - dob_date.year
        if today.month < dob_date.month or (today.month == dob_date.month and today.day < dob_date.day):
            age -= 1
        return age

    @property
    def client_code(self):
        return self._client_code
    
    @client_code.setter
    def client_code(self,valor):
        self._client_code=valor

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,valor):
        self._name=valor

    @property
    def dob(self):
        dob = datetime.date.fromisoformat(self._dob)
        self._dob = dob
        return self._dob
    
    @dob.setter
    def dob(self,valor):
        dob = datetime.date.fromisoformat(valor)
        self._dob = dob
    
    @property
    def idade(self):
        return self._idade

