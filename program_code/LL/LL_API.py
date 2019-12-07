from LL.WorktripLL import *
from LL.DestinationLL import *
from LL.EmployeeLL import *
from LL.AirplanesLL import *
from LL.LL_functions import *

class LL_API:

#From UI: create("employee",(ssn,name,address,mobile,email,role,rank,licence))
    def create(self, keyword,user_input):    
        '''Creates new object and saves to Database. \n
        keyword: employee,airplane,destination or worktrip
        \n
        user_input: user input for corresponding item as tuple
        '''
        if keyword == 'employee':
            cr_emp = EmployeeLL()
            cr_emp.create_employee(user_input)

        elif keyword == 'airplane':
            cr_air = AirplanesLL()
            cr_air.create_airplane(user_input)

        elif keyword == 'destination':
            cr_dest = DestinationLL()
            cr_dest.create_destination(user_input)

        elif keyword =='worktrip':
            cr_trip = WorktripLL()
            cr_trip.create_worktrip(user_input)   


    def get_list(self,keyword):
            '''Gets updated list from database. \n
                keyword: employee,airplane,destination or worktrip
            '''
            updated_list = []
            
            new_instance = LL_functions()
            updated_list =new_instance.get_updated_list_from_DB(keyword)
            return updated_list
            




def testmain():
    new = LL_API()
   
#    new.create('airplane', ('32','rass','re re','re 31','er','asdf@gmail.com')) #airplane nyskraning test
#    new.create('employee', ('0','4455668855','aparassgat Helga','Hehe 31','8453474','eythoroli95@gmail.com','Pilot','Copilot','Fokker232'))
    new.create('destination',('11','asdf','Greenland','1:00:55','1.343','Hraði Brunann','328738975','flugvolllur'))












# #Staff functions
# #----------------------------------------------------------------------------------------------
# def create_employee(ssn,name,address,mobile,email,role,rank,licence):
#     """Creates a new employee, returns updated list of employees."""      
    
#     EmployeeLL.save_employee(ssn,name,address,mobile,email,role,rank,licence)

#     # new_emp = Employee(ssn,name,address,mobile,email,role,rank,licence)
#     updated_list = EmployeeLL.get_employee_list()
#     return updated_list

# def change_employee(self,ssn,name,address,mobile,email,role,rank,licence):
#     """Changes information about employee, except ssn, name or creation date."""
#     #old_info = EmployeeFile(fieldname="ssn",searchparam=ssn)
#     new_info = Employee(ssn,name,address,mobile,email,role,rank,licence)

#     EmployeeLL.change_info(old_info,new_info)

#     #old_info = EmployeeFile(fieldname="ssn",searchparam=ssn)
#     line_number = old_info.run_me()

#     data_string = ",".join([ssn,name,address,mobile,email,role,rank,licence])

#     new_info = EmployeeFile(line_to_replace=line_number,replace_with=data_string)
#     new_info.run_me()


# #----------------------------------------------------------------------------------------------
# #Airplanes

# def get_airplane_types():
#     all_planes = Airplane.get_airplane_list()
#     filtered_planes =Airplane.filter_planes(all_planes, model)
#     return filtered_planes

# def get_all_airplanes():
#     all_planes = get_all_planes()
#     return all_planes

# def create_airplane(planeID, planeType, manufacturer, model, name, capacity):
#     save_airplane(planeID, planeType, manufacturer, model, name, capacity)
    
    
# #if __name__ == "__main__":


#     #main()



# #new_emp = '2501952149,Eyþór Óli Borgþórsson,Þingás 31,8453474,eythoroli95@gmail.com,Pilot,Copilot,Fokker232'
# emp = create_employee("2501952149","Eyþór Óli Borgþórsson","Þingás 31","8453474","eythoroli95@gmail.com","Pilot","Copilot","Fokker232")

# print(emp)
