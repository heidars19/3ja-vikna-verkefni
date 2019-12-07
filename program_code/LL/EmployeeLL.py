from DB.DATA_API import *
from LL.Employee import *
from LL.LL_functions import *

#from DB.AirplaneFile import AirplaneFile

class EmployeeLL(LL_functions):

    def create_employee(self,personal_identity):
    #def create_employee(self,ssn,name,address,mobile,email,role,rank,licence):
        """Creates a new employee and saves to database.""" 

        new_emp = Employee(*personal_identity, registration_date='')
        registration_str = new_emp.get_registration_str()

        print("EmployeeLL")
        save = self.save_object_to_DB("employee",registration_str)
        return save


    def change_employee(self,registered_identity):
        """Changes information about employee, except ssn, name or creation date."""

        ssn,name,address,mobile,email,role,rank,licence,registration_date = registered_identity
        changed_emp = Employee(ssn,name,address,mobile,email,role,rank,licence,registration_date)

        self.change_object_in_DB("employee",str(changed_emp),self.id)


    #def __init__ (self, data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None ) :

#     def __init__(self,emp_info,new_info =None,old_info=None):

#         ssn,name,address,mobile,email,role,rank,licence = emp_info.split(',')

#         self.emp_info = emp_info
#         self.new_info = new_info
#         self.old_info = old_info
#         self.employee = Employee(ssn,name,address,mobile,email,role,rank,licence)

#     def save_employee(self,ssn,name,address,mobile,email,role,rank,licence):
#         new_emp = Employee(ssn,name,address,mobile,email,role,rank,licence )
#         log_emp = EmployeeFile(data_to_append=str(new_emp))
#         log_emp.start()

#     def get_updated_list():
#         new_emp_list = EmployeeFile()               #create new instance
#         updated_list = new_emp_list.start()      
#         return updated_list


#     def change_employee(self,old_info,new_info):
#         '''Checks if user is trying to change invalid information'''
        
#         ssn,name,address,mobile,email,role,rank,licence = new_info.split(',')

#         old_info = EmployeeFile(fieldname="ssn",searchparam=ssn)
#     pass


# def get_employee_list():
#     new_emp_list = EmployeeFile()
#     get_emp_list = new_emp_list.start()
#     #newemp_list = start.EmployeeFile()

# return get_emp_list

# def assign_worktrip(self,worktrip):
#     pass

# def write_personalinfo(self):
#     #Save information about employee to database
#     data_to_append = str(self)
#     name_of_file = "Employees"
#     return append_data_to_file(data_to_append, name_of_file, header="")
#     pass
    
# def check_ssn(self,ssn):
#     #tala við database - láta fá kennitölu og fá true eða false
#     if false:
#         write_personalinfo(self)
#     else:
#         return True
#     pass


# def append_data_to_file(self): 

#     pass

# def read_line_in_file(self, data):
#     pass

# def change_line(self,line,filename,):
#     pass

# str(newemp)
