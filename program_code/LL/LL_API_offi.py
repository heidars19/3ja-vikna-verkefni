from LL.WorktripLL import *
from LL.DestinationLL import *
from LL.EmployeeLL import *
from LL.AirplanesLL import *

class LL_API_offii:

#create("employee",(ssn,name,address,mobile,email,role,rank,licence))
    def create(self,keyword,user_input):
        '''Creates new object and saves to Database. \n
        keyword: employee,airplane,destination or worktrip
        \n
        user_input: user input for corresponding item
        '''
        if keyword == 'employee':
            cr_emp = EmployeeLL()
            cr_emp.create_employee(user_input)

        elif keyword == 'airplane':
            cr_air = AirplanesLL()
            cr_air.create_airplane(user_input)

        elif keyword == 'destination':
            cr_dest = Des1tinationLL()
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
            















