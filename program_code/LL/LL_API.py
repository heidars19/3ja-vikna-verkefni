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
        user_input: user input for corresponding item as tuple. No id or registration date.
        '''
        if keyword == 'employee':
            cr_emp = EmployeeLL()
            run_create = cr_emp.create_employee(user_input)

        elif keyword == 'airplane':
            cr_air = AirplanesLL()
            run_create = cr_air.create_airplane(user_input)

        elif keyword == 'destination':
            cr_dest = DestinationLL()
            run_create = cr_dest.create_destination(user_input)

        elif keyword =='worktrip':
            cr_trip = WorktripLL()
            run_create = cr_trip.create_worktrip(user_input)  

        return run_create

    def change(self,keyword,changed_object):
        '''Changes object in Database. \n
        keyword[str]: employee,airplane,destination or worktrip
        \n
        changed_object[tuple]: Changed object, including id and registration date.
        '''
        if keyword == 'employee':
            ch_emp = EmployeeLL()
            run_change = ch_emp.change_employee(changed_object)

        elif keyword == 'airplane':
            ch_air = AirplanesLL()
            run_change = ch_air.change_airplane(changed_object)

        elif keyword == 'destination':
            ch_dest = DestinationLL()
            run_change = ch_dest.change_destination(changed_object)

        elif keyword == 'worktrip':
            ch_work = WorktripLL()
            run_change = ch_work.change_worktrip(changed_object)

        return run_change

    def get_list(self,keyword,list_type="",searchparam = ""):
            '''Gets updated list from database. \n
               keyword[str]: employee,airplane,destination,worktrip \n
                \n
           
                TO GET LIST OF EMPLOYEES WORKING ON SPECIFIC DATE AND THEIR DESTINATIONS: \n
                keyword = 'worktrip', list_type = 'working_employees', searchparam = 'YYYY-MM-DD' \n

                TO GET LIST OF EMPLOYEES AVAILABLE ON SPECIFIC DATE \n
                keyword = 'worktrip', list_type = 'available_employees', searchparam = 'YYYY-MM-DD' \n
                
                TO GET LIST OF UNIQUE TYPES OF REGISTERED AIRPLANES\n
                keyword = 'airplane', list_type = 'plane_licences" Returns list of unique types of registered airplanes.
            '''

            if list_type == "working_employees" or "available_employees":
                new_instance = WorktripLL()
                emp_by_date_list = new_instance.get_emp_by_date(keyword,list_type,searchparam)
            
                return emp_by_date_list
            

            elif list_type == "plane_licences":
                new_instance = AirplanesLL()
                plane_licence = new_instance.get_plance_licence(keyword, list_type)

                return plane_licence
                
            else:
                updated_list = []
                new_instance = LL_functions()
                updated_list = new_instance.get_updated_list_from_DB(keyword)
                updated_list.pop(0)
        
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
