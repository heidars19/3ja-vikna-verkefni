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

        elif worktrip == "worktrip":
            save_obj = WorkTripFile(data_to_append=object_instance)
        else:
            return "There is no such object type as" + str(keyword) + "Change keyword - should be string."

        save_obj.start()
        return True

    def change_object_in_DB(self,keyword,object_instance):
        '''Changes personal information about employee, except ssn, name and creation_date'''

        new_file = StaffFile(fieldname="ssn",searchparam=self.ssn) #Looks for ssn in StaffFile and returns line number
        line_number = new_file.start()
        update_line = StaffFile(line_to_replace=line_number,replace_with=str(self))
        update_line.start()

    def get_updated_list_from_DB(self,keyword):
        '''Returns updated list from database \n
            keyword: employee, airplane, destionation or worktrip
            '''
<<<<<<< HEAD
        updated_list = []
        if keyword == "Employee":
            new_instance = StaffFile()               #create new instance
            updated_list = new_instance.start() 
            new_list = []
            for x in updated_list:
                new_list.append(x.split(','))
=======

        if keyword == "Employee":
            new_emp_list = StaffFile()               #create new instance
            updated_list = new_emp_list.start()      
>>>>>>> 60d4b6aeea56f561416095b96abd27e3b75d2a3a
        return updated_list


   # def change_object_in_DB(self,keyword,object_instance)