
import DB.DATA_API

class Employee:
    """This class represents the Employees of Nan Air and keeps track of their information."""


    def __init__(self,ssn,name,address,mobile,email,role,rank,licence): 
        from datetime import date
        today = date.today()

        self.__ssn = ssn
        self.__name = name
        self.address = address
        self.mobile = mobile
        self.email = email
        self.role = role
        self.rank = rank
        self.licence = licence
        self.__creationdate = today

    def __str__(self):
        return f'{self.__ssn},{self.__name},{self.address},{self.mobile},{self.email},{self.role},{self.rank},{self.licence},{self.__creationdate}'

    #def __repr__(self):
     #   return Employee({self.__ssn},{self.__name},{self.address},{self.mobile},{self.email},{self.role},{self.rank},{self.licence},{self.__creationdate})

    #name getterar fyrir privat breytur
    @property 
    def ssn(self):
        return self.__ssn
    @property
    def name(self):
        return self.__name
    @property
    def creationdate(self):
        return self.__creationdate

    #name setter fyrir privat breytur
    @ssn.setter 
    def ssn(self,ssn):
        self.__ssn = ssn

    @name.setter
    def name(self,name):
        self.__name = name
    
    @creationdate.setter
    def creationdate(self,creationdate):
        self.__creationdate = creationdate

    @classmethod
    def from_string(cls,emp_string):
        ssn,name,address,mobile,email,role,rank,licence = emp_string.split(',')
        return cls(ssn,name,address,mobile,email,role,rank,licence)


new_emp = '2501952149,Eyþór Óli Borgþórsson,Þingás 31,8453474,eythoroli95@gmail.com,Pilot,Copilot,Fokker232'
newemp = Employee.from_string(new_emp)
print(newemp)




