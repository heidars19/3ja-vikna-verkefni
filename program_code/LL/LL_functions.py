from DB.DATA_API import *

class LL_functions():
    #Call this function from EmployeeLL,DestionationLL,... Example: save_object_to_DB("employee", str(emp))
    def save_object_to_DB(self,keyword,object_instance):
        '''Saves new object to database. \n
        \n Returns True if operation successful.
        keyword: employee,airplane,destination or worktrip as string
        \n 
        object_instance: Instance of employee, airplane, destination or worktrip as string. 
        '''
        if keyword == "employee":
            save_obj = StaffFile(data_to_append=object_instance)
       
        elif keyword == "destination":
            save_obj = DestinationFile(data_to_append=object_instance)

        elif keyword == "airplane":
            save_obj = AirplaneFile(data_to_append=object_instance)

        elif keyword == "worktrip":
            save_obj = WorkTripFile(data_to_append=object_instance)
        else:
            return "There is no such object type as" + str(keyword) + "Change keyword - should be string."

        save_obj.start()

    #Example: change_object_in_DB(employee,emp1,ssn,emp1_ssn)
    def change_object_in_DB(self,keyword,object_instance,object_id):
        '''Changes information about object in Database. \n
                keyword: employee, destination, airplane, worktrip \n
        '''

        new_file = StaffFile(fieldname="id",searchparam=object_id) #Looks for ssn in StaffFile and returns line number
        line_number = new_file.start()

        update_line = StaffFile(line_to_replace=line_number,replace_with=object_instance)
        update_line.start()






    def get_updated_list_from_DB(self,keyword):
        '''Returns updated list from database \n
            keyword: employee, airplane, destionation or worktrip
            '''
        updated_list = []

        if keyword == "employee":
            new_instance = StaffFile()               #create new instance
            updated_list = new_instance.start() 
            new_list = []
            for x in updated_list:
                new_list.append(x.split(','))

        elif keyword == "worktrip":
            new_instance = WorkTripFile()               #create new instance
            updated_list = new_instance.start() 
            new_list = []
            for x in updated_list:
                new_list.append(x.split(','))

        elif keyword == "destination":
            new_instance = DestinationFile()               #create new instance
            updated_list = new_instance.start() 
            new_list = []
            for x in updated_list:
                new_list.append(x.split(','))

        elif keyword == "airplane":
            new_instance = AirplaneFile()               #create new instance
            updated_list = new_instance.start() 
            new_list = []
            for x in updated_list:
                new_list.append(x.split(','))

        return new_list
