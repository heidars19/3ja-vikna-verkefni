from DB.DATA_API import *

class Employee:
    """This class represents the Employees of Nan Air and keeps track of their information."""

    def __init__(self,ssn,name,address,mobile,email,role,rank,licence,registration_date=""): 
        from datetime import date
        #today = date.today()

        self._id = _id
        self.__ssn = ssn
        self.__name = name
        self.address = address
        self.mobile = mobile
        self.email = email
        self.role = role
        self.rank = rank
        self.licence = licence
        self.__registration_date = registration_date

    def registration(self):
        return f'{self.__ssn},{self.__name},{self.address},{self.mobile},{self.email},{self.role},{self.rank},{self.licence}'

    def change_registration(self):
        return f'{self._id},{self.__ssn},{self.__name},{self.address},{self.mobile},{self.email},{self.role},{self.rank},{self.licence},{self.__registration_date}'

    #name getterar fyrir privat breytur
    @property 
    def ssn(self):
        return self.__ssn
    @property
    def name(self):
        return self.__name

#    # @property
#   def creationdate(self):
#   return self.__creation_date

    #name setter fyrir privat breytur
    # @ssn.setter 
    # def ssn(self,ssn):
    #     self.__ssn = ssn

    # @name.setter
    # def name(self,name):
    #     self.__name = name
    
    # @creationdate.setter
    # def creationdate(self,creation_date):
    #     self.__creation_date = creation_date

    @classmethod
    def from_string(cls,emp_string):
        ssn,name,address,mobile,email,role,rank,licence = emp_string.split(',')
        return cls(ssn,name,address,mobile,email,role,rank,licence)

#---------------------------------FUNCTIONS FOR EMPLOYEES-----------------------------------------------------#

    # def save_employee(self):
    #     '''Save new employee to database'''
    #     print(self)
    #     log_emp = EmployeeFile(data_to_append=str(self))
    #     log_emp.start()

    # def change_employee(self):
    #     '''Changes personal information about employee, except ssn, name and creation_date'''

    #     new_file = EmployeeFile(fieldname="ssn",searchparam=self.ssn) #Looks for ssn in EmployeeFile and returns line number
    #     line_number = new_file.start()
    #     update_line = EmployeeFile(line_to_replace=line_number,replace_with=str(self))
    #     update_line.start()
        
    def error_check(self):
        '''Defensive programming: Checks if errors in user input.'''
        ssn = check_ssn(self.ssn)
        address = check_address(self.address)
        email = check_email(self.email)
        cellphone = check_cellphone(self.check_cellphone)

        print(ssn, '&',address,'&',email,'&',cellphone)


# new_emp = '2501952149,Eyþór Óli Borgþórsson,Þingás 31,8453474,eythoroli95@gmail.com,Pilot,Copilot,Fokker232'
# newemp = Employee.from_string(new_emp)
# print(newemp)




