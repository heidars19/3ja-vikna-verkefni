from DB.DATA_API import *

class LL_functions():

    def file_type(self,keyword):

        file_type = ""

        if keyword == "employee":
            file_type = EmployeeFile

        elif keyword == "destination":
            file_type = DestinationFile

        elif keyword == "airplane":
            file_type = AirplaneFile

        elif keyword == "worktrip":
            file_type = WorkTripFile

        elif keyword == "worktripold":
            file_type = WorkTripFileOld

        else:
            return f"There is no such object type as {keyword}. Change keyword - should be string."

        return file_type

    #Call this function from EmployeeLL,DestionationLL,... Example: save_object_to_DB("employee", str(emp))
    def save_object_to_DB(self, keyword,object_instance):
        '''Saves new object to database. \n
        \n Returns True if operation successful.
        keyword: employee,airplane,destination or worktrip as string
        \n 
        object_instance: Instance of employee, airplane, destination or worktrip as string. 
        '''

        file_name = self.file_type(keyword)
        save_obj = file_name(data_to_append=object_instance)

        run_save = save_obj.start()
      
        return run_save

    #Example: change_object_in_DB(employee,emp1,ssn,emp1_ssn)
    def change_object_in_DB(self, keyword, new_string, string_id):
        '''Changes information about object in Database. \n
                keyword: employee, destination, airplane, worktrip \n
        '''
        file_name = self.file_type(keyword)

        new_file = file_name(fieldname="id",searchparam=string_id) #looks for id and returns line number
        line_number = new_file.start()

        update_line = file_name(line_to_replace=line_number,replace_with=new_string)
        return_value = update_line.start()

        return return_value


    def get_updated_list_from_DB(self,keyword):
        '''Returns updated list from database \n
            keyword: employee, airplane, destionation or worktrip
            '''
        file_name = self.file_type(keyword)

        new_instance = file_name()
        updated_list = new_instance.start() 
        new_list = []
        for i in updated_list:
            new_list.append(i.split(','))

        return new_list