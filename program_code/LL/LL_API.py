from LL.WorktripLL import *
from LL.DestinationLL import *
from LL.EmployeeLL import *
from LL.AirplanesLL import *
from LL.LL_functions import *
from datetime import datetime

class LL_API:

    
    def return_msg(self, msg, keyword=''):
        '''
        Replaces numeric error messages to strings
        '''
        if msg == 1:
            return "Success in {}".format(keyword)
        elif msg == 0 :
            return "No success in {}".format(keyword)
        elif msg == -1 :
            return "An unknow error occurred while {}".format(keyword)
        elif msg == -404 :
            return "File not Found error on {}".format(keyword)
        else:
            return "An unknow error occurred or not getting return value from DB"
        return


    def create(self, keyword,user_input):    
        '''
        Creates new object and saves to Database. Returns msg with success or error. \n
        keyword [string]: 'employee', 'airplane', 'destination', 'worktrip'\n
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

    def change(self,keyword, line_to_change_tuple):
        '''
        Changes a line in the database.\n
        keyword [string]: 'employee', 'airplane', 'destination', 'worktrip'\n
        line_to_change_tuple [tuple]: User input for changed object including id and registration date.
        '''

        if keyword == 'employee':
            ch_emp = EmployeeLL()
            run_change = ch_emp.change_employee(line_to_change_tuple)

        elif keyword == 'airplane':
            ch_air = AirplanesLL()
            run_change = ch_air.change_airplane(line_to_change_tuple)

        elif keyword == 'destination':
            ch_dest = DestinationLL()
            run_change = ch_dest.change_destination(line_to_change_tuple)

        elif keyword == 'worktrip':
            ch_work = WorktripLL()
            run_change = ch_work.add_employees_worktrip(line_to_change_tuple)

        return run_change

    def get_list(self,keyword='',list_type="",searchparam = "", _id='', role='',rank='', a_license='', days=7):
            '''
            Gets lists from database. \n
            keyword [string]: 'employee', 'airplane', 'destination', 'worktrip'\n
        
            LIST OF EMPLOYEES WORKING ON SPECIFIC DATE AND THEIR DESTINATIONS: \n
            keyword = 'worktrip', list_type = 'working_employees', searchparam = 'YYYY-MM-DD' \n

            LIST OF EMPLOYEES AVAILABLE ON SPECIFIC DATE \n
            keyword = 'worktrip', list_type = 'available_employees', searchparam = 'YYYY-MM-DD' \n
            
            LIST OF UNIQUE TYPES OF REGISTERED AIRPLANES\n
            keyword = '', list_type = 'plane_licences" \n

            LIST OF WORKSCHEDULE FOR A SPECIFIC EMPLOYEE \n
            keyword = '', list_type = 'work_schedule'\n

            LIST OF WORKTRIPS BY DATE \n
            keyword = '', list_type = 'worktrips_by_date', searchparam = 'YYYY-MM-DD'\n

            DESTINATION ID \n
            keyword = '', list_type = "destination_id" \n

            READABLE WORKTRIP INFO WITH NAMES NOT IDS \n
            keyword = list_type = ""worktrip_readable", searchparam = (info that needs to be translated)
            '''
            if list_type == "working_employees":
                worktrip_instance = WorktripLL()
                emp_instance = EmployeeLL()
                get_emp_dest_date = worktrip_instance.get_emp_dest_date(searchparam)
                employee_list = []
                working_staff_list = emp_instance.working_employees(get_emp_dest_date)
                destination_inst = DestinationLL()

                for employee_info in working_staff_list:
                    employeee, role, destination_id = employee_info
                    destination_name = destination_inst.find_name_by_id(destination_id)
                    employee_list.append(["",employeee, role,'', destination_name, '']) 
                return_value = employee_list
                       

            elif list_type == "available_employees":
                employee_list = []
                worktrip_instance = WorktripLL()
                busy_staff = worktrip_instance.get_emp_dest_date(searchparam, include_arrivaldate=True) # Busy pilots
                emp_instance = EmployeeLL()
                available_staff = emp_instance.available_employees(busy_staff) # All pilots
                employee_list = emp_instance.find_qualified_staff(available_staff, role, rank, a_license)
            
                return_value = employee_list

            elif list_type == "worktrips_by_date":
        
                new_instance = WorktripLL()
                worktrips_by_date = new_instance.get_worktrips_by_date(searchparam, days)

                return_value = worktrips_by_date

            elif list_type == "plane_licences":
                new_instance = AirplanesLL()
                plane_licence = new_instance.get_plane_licence()
                return_value = plane_licence

            elif list_type == "available_planes":
                new_instance = AirplanesLL()
                available_planes = new_instance.get_available_planes(searchparam,_id) #datetime and airplane id
                return_value = available_planes

            elif list_type == "work_schedule":
                new_instance = WorktripLL()
                workschedule = new_instance.get_workschedule(searchparam,_id,days) #searchparam is the date, the _id is the staffmemebers id.
                return_value = workschedule

            elif list_type == "destination_id":
                new_instance = DestinationLL()
                destination_id = new_instance.get_destination_id(searchparam)
                return_value = destination_id

            elif list_type == "destination_name":
                new_instance = DestinationLL()
                destination_id = new_instance.find_name_by_id(searchparam)
                return_value = destination_id

            elif list_type =="worktrip_readable":  #Display in TUI, get names of destinations and airplanes that are referenced with ID´s in Worktrip Database
                
                airplane_inst = AirplanesLL()
                destination_inst = DestinationLL()
                employee_inst = EmployeeLL()

                worktrip = Worktrip(*searchparam)

                worktrip.aircraft_id = airplane_inst.find_name_by_id(worktrip.aircraft_id)
                worktrip.arriving_at = destination_inst.find_name_by_id(worktrip.arriving_at)
                worktrip.captain = employee_inst.find_name_by_id(worktrip.captain)
                worktrip.copilot = employee_inst.find_name_by_id(worktrip.copilot)
                worktrip.fsm = employee_inst.find_name_by_id(worktrip.fsm)
                worktrip.fa1 = employee_inst.find_name_by_id(worktrip.fa1)
                worktrip.fa2 = employee_inst.find_name_by_id(worktrip.fa2)

                return_value = worktrip.get_changes_registration_str().split(',')
                
            elif list_type == "pilot_licences":
                new_instance = EmployeeLL()
                return_value = new_instance.find_pilot_with_license(a_license)

            else:
                updated_list = []
                new_instance = LL_functions()
                updated_list = new_instance.get_updated_list_from_DB(keyword)
                if len(updated_list) > 0 :
                    updated_list.pop(0)
        
                return_value = updated_list

            if isinstance(return_value, int) :
                return [[self.return_msg(return_value, keyword)]]
                
            return return_value
        
