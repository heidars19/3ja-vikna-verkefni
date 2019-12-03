class Employee:
    """This class represents the Employees of Nan Air and keeps track of their information."""
    def __init__(self,ssn,name,address,mobile,email,role,rank,licence): 
        from datetime import date
        today = date.today()

        self.__ssn = ssn
        self.__name = name
        self.__address = address
        self.__mobile = mobile
        self.__email = email
        self.__role = role
        self.__rank = rank
        self.__licence = licence
        self.__creationdate = today

    def __str__(self):
        return f'{self.__ssn},{self.__name},{self.__address},{self.__mobile},{self.__email},{self.__role},{self.__rank},{self.__licence}'

    def __repr__(self):
        return Employee({self.__ssn},{self.__name},{self.__address},{self.__mobile},{self.__email},{self.__role},{self.__rank},{self.__licence})'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    """def change_employee(self):
        self.personalinfo[infotype] = new_info
        pass

    def assign_worktrip(self,worktrip):
        self.worktrip = worktrip
        pass

    def get_personalinfo(self,ssn):
        return f"{self.__ssn},{self.__name},{self.__address},{self.mobile},{self.email},{self.role},{self.rank},{self.licence}"

    def write_personalinfo(self):
        Save information about employee to database
        data_to_append = str(self)
        name_of_file = "Employees"
        return append_data_to_file(data_to_append, name_of_file, header="")
        
    def check_ssn(self,ssn):
        #tala við database - láta fá kennitölu og fá true eða false
        if false:
            write_personalinfo(self)
        else:
            return True"""


eythor = Employee('2501952149','Eyþór Óli Borgþórsson','Þingás 31','8453474','eythoroli95@gmail.com', 'Pilot', 'Copilot', 'Fokker232')
print(eythor)
print(eythor.name)
eythor.name = "Sigurgeir"
print(eythor)