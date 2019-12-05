from Employee import *
from EmployeeLL import *
#from DB.DATA_API import * eigum ekki að tala beint við db
from Airplanes import *
from Destination import *


#Staff functions
#----------------------------------------------------------------------------------------------
def create_employee(ssn,name,address,mobile,email,role,rank,licence):
    """Creates a new employee, returns updated list of employees."""      
    
    EmployeeLL.save_employee(ssn,name,address,mobile,email,role,rank,licence)

    # new_emp = Employee(ssn,name,address,mobile,email,role,rank,licence)
    updated_list = EmployeeLL.get_employee_list()
    return updated_list

def change_employee(self,ssn,name,address,mobile,email,role,rank,licence):
    """Changes information about employee, except ssn, name or creation date."""
    #old_info = StaffFile(fieldname="ssn",searchparam=ssn)
    new_info = Employee(ssn,name,address,mobile,email,role,rank,licence)

    EmployeeLL.change_info(old_info,new_info)

    #old_info = StaffFile(fieldname="ssn",searchparam=ssn)
    line_number = old_info.run_me()

    data_string = ",".join([ssn,name,address,mobile,email,role,rank,licence])

    new_info = StaffFile(line_to_replace=line_number,replace_with=data_string)
    new_info.run_me()


#----------------------------------------------------------------------------------------------

#Airplanes

def get_airplane_types():
    all_planes = Airplane.get_airplane_list()
    filtered_planes =Airplane.filter_planes(all_planes, model)
    return filtered_planes

def get_all_airplanes():
    all_planes =  get_all_planes()
    return all_planes

def create_airplane(planeID, planeType, manufacturer, model, name, capacity):
    save_airplane(planeID, planeType, manufacturer, model, name, capacity)
    
    



    



    

#if __name__ == "__main__":


    #main()



#new_emp = '2501952149,Eyþór Óli Borgþórsson,Þingás 31,8453474,eythoroli95@gmail.com,Pilot,Copilot,Fokker232'
emp = create_employee("2501952149","Eyþór Óli Borgþórsson","Þingás 31","8453474","eythoroli95@gmail.com","Pilot","Copilot","Fokker232")

print(emp)
