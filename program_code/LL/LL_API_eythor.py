from LL.EmployeeLL import *
from LL.LL_functions import *
from LL.AirplanesLL import *
from EmployeeLL import *
from DB.DATA_API import * eigum ekki að tala beint við db
from Airplanes import *
from AirplanesLL import *
from Destination import *
from DestinationLL import *
 
class LL_API_eythor:

    def create(self,keyword,user_input):    #create("employee",(ssn,name,address,mobile,email,role,rank,licence))
        '''Creates new item and saves to Database. \n
        \n Returns True if operation successful.
        
        keyword: employee,airplane,destination or worktrip
        \n
        user_input: user input for corresponding item
        '''
        if keyword == 'employee':
            cr_emp = EmployeeLL()
            cr_emp.create_employee(user_input)

        if keyword == 'airplane':
            cr_air == AirplanesLL()
            cr_air.create_airplane(user_input)

        if keyword == 'destination':
            cr_dest == DestinationLL()
            cr_dest.create_destination(user_input)

        if keyword =='worktrip':
            cr_trip == WorktripLL()
            cr_trip.create_worktrip(user_input)   

    def change(self,keyword,user_input):
        
        #ssn,name,address,mobile,email,role,rank,licence,registration_date = data_info

        if user_input == 'employee':
            ch_emp == EmployeeLL()
            #ch_emp.change_employee(ssn,name,address,mobile,email,role,rank,licence,registration_date)
            ch_emp.change_employee(user_input)

    def get_list(self,keyword):
        '''Gets updated list from database. \n
        
        keyword: employee,airplane,destination or worktrip
        \n
        user_input: user input for corresponding item
        '''

        updated_list = []
        
        new_instance = LL_functions()
        updated_list =new_instance.get_updated_list_from_DB(keyword)
        return updated_list
        # emp_updated_list = []

        # if keyword == 'employee': 
        #     emp_list = LL_functions()
        #     emp_updated_list = emp_list.get_updated_list_from_DB(keyword)
        #     emp_updated_list.pop(0)
     
        # elif keyword == 'worktrip': 
        #     work_list = LL_functions()
        #     emp_updated_list = emp_list.get_updated_list_from_DB(keyword)
        #     emp_updated_list.pop(0)

        # elif keyword == 'destination':
        #     dest_list = LL_functions()
        #     emp_updated_list = emp_list.get_updated_list_from_DB(keyword)
        #     emp_updated_list.pop(0)
           
        # return emp_updated_list

        



#Staff functions
#----------------------------------------------------------------------------------------------
# def create_employee(ssn,name,address,mobile,email,role,rank,licence):
#     """Creates a new employee, returns updated list of employees."""      
    
#     new_emp = Employee(ssn,name,address,mobile,email,role,rank,licence)
#     new_emp.save_employee()
#     # updated_list = new_emp.get_employee_list()
#     # return updated_list
    
# def change_employee(ssn,name,address,mobile,email,role,rank,licence,registration_date):
#     """Changes information about employee, except ssn, name or creation date."""

#     changed_emp = Employee(ssn,name,address,mobile,email,role,rank,licence,registration_date)
#     changed_emp.change_employee()
#     #updated_list = Employee.get_employee_list
#     #return updated_list



# def main():
# #new_emp = '2501952149,Eyþór Óli Borgþórsson,Þingás 31,8453474,eythoroli95@gmail.com,Pilot,Copilot,Fokker232'
#     emp = create_employee("2501952149","Eyþór Óli Borgþórsson","Þingás 31","8453474","eythoroli95@gmail.com","Pilot","Copilot","Fokker232")

#     print(emp)
#     return
  #  new_emp = '2501952149','Eyþór Óli Borgþórsson','Þingás 31','8453474','eythoroli95@gmail.com','Pilot','Copilot','Fokker232'
  # 
  
def main():
    create_employee('2501952149','Eyþór Óli Borgþórsson','Þingás 31','8453474','eythoroli95@gmail.com','Pilot','Copilot','Fokker232')
    return

if __name__ == "__main__":
    main()