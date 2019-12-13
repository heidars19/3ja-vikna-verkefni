from LL.WorktripLL_sigurgeir import *
from LL.DestinationLL import *
from LL.EmployeeLL import *
from LL.AirplanesLL import *
from LL.LL_functions import *

class LL_API:

    def create(self, keyword,user_input):    
        '''
        \n Creates new object and saves to Database. Returns msg with success or error. \n
        keyword [string]: employee /airplane / destination / worktrip\n
        user_input [tuple]: User input for corresponding item as tuple with a leading empty string.
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
        '''
        \n Changes object in Database. Returns msg with success or error. \n
        keyword [string]: employee /airplane / destination / worktrip\n
        changed_object [tuple]: User input for changed object with including id and registration date.
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

    def get_list(self,keyword,list_type="",searchparam = "", _id='', role='',rank='', a_license=''):
            '''
            Gets lists from database. \n
            keyword [string]: employee /airplane / destination / worktrip\n
                \n
           
                LIST OF EMPLOYEES WORKING ON SPECIFIC DATE AND THEIR DESTINATIONS: \n
                keyword = 'worktrip', list_type = 'working_employees', searchparam = 'YYYY-MM-DD' \n

                LIST OF EMPLOYEES AVAILABLE ON SPECIFIC DATE \n
                keyword = 'worktrip', list_type = 'available_employees', searchparam = 'YYYY-MM-DD' \n
                
                LIST OF UNIQUE TYPES OF REGISTERED AIRPLANES\n
                keyword = '', list_type = 'plane_licences" \n

                LIST OF WORKSCHEDULE FOR A SPECIFIC EMPLOYEE \n
                keyword = '', list_type = 'work_schedule'

                DESTINATION ID \n
                keyword = '', list_type = 
            '''

            if list_type == "working_employees" or list_type == "available_employees": 
                
                employee_list = []
                new_instance = WorktripLL()
                get_emp_dest_date = new_instance.get_emp_dest_date(keyword,searchparam)
                new_instance = EmployeeLL()

                if list_type == "working_employees":
                        employee_list = new_instance.working_employees(get_emp_dest_date)       

                elif list_type == "available_employees":
                        employee_list = new_instance.available_employees(get_emp_dest_date, role, rank, a_license)
                        
                return employee_list

            elif list_type == "plane_licences":
                new_instance = AirplanesLL()
                plane_licence = new_instance.get_plane_licence()
                return plane_licence

            elif list_type == "available_planes":
                new_instance = AirplanesLL()
                available_planes = new_instance.get_available_planes(searchparam,_id) #datetime and airplane id
                return available_planes

            elif list_type == "work_schedule":
                new_instance = WorktripLL()
                workschedule = new_instance.get_workschedule(searchparam,_id) #searchparam is the date, the _id is the staffmemebers id.
                return workschedule

            elif list_type == "destination_id":
                new_instance = DestinationLL()
                destination_id = new_instance.get_destination_id(searchparam)
                return destination_id

            elif list_type == "covert_id_to_names":
                new_instance = Dest

            else:
                updated_list = []
                new_instance = LL_functions()
                updated_list = new_instance.get_updated_list_from_DB(keyword)
                updated_list.pop(0)
        
                return updated_list

def testmain():
    new = LL_API()
   