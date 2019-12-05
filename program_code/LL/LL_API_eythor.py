from LL.Employee import *
#from EmployeeLL import *
#from DB.DATA_API import * eigum ekki að tala beint við db
# from Airplanes import *
# from AirplanesLL import *
# from Destination import *
# from DestinationLL import *

#Staff functions
#----------------------------------------------------------------------------------------------
def create_employee(ssn,name,address,mobile,email,role,rank,licence):
    """Creates a new employee, returns updated list of employees."""      
    
    new_emp = Employee(ssn,name,address,mobile,email,role,rank,licence)
    new_emp.save_employee()
    # updated_list = new_emp.get_employee_list()
    # return updated_list
    
def change_employee(self,ssn,name,address,mobile,email,role,rank,licence):
    """Changes information about employee, except ssn, name or creation date."""

    changed_emp = Employee(ssn,name,address,mobile,email,role,rank,licence)
    changed_emp.change_employee()
    updated_list = Employee.get_employee_list
    return updated_list


# def main():
# #new_emp = '2501952149,Eyþór Óli Borgþórsson,Þingás 31,8453474,eythoroli95@gmail.com,Pilot,Copilot,Fokker232'
#     emp = create_employee("2501952149","Eyþór Óli Borgþórsson","Þingás 31","8453474","eythoroli95@gmail.com","Pilot","Copilot","Fokker232")

#     print(emp)
#     return



# if __name__ == "__main__":
#     main()