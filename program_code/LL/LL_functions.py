from DB.DATA_API import *

class LL_functions():

    def file_type(keyword):
        if keyword == "employee":
            file_type = EmployeeFile

        elif keyword == "destination":
            file_type = DestinationFile

        elif keyword == "airplane":
            file_type = AirplaneFile

        elif keyword == "worktrip":
            file_type = WorkTripFile

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
        new_file = ""

        new_file = file_type(keyword)

        # if keyword == "employee":
        #     file_type = EmployeeFile
p
        # elif keyword == "destination":
        #     file_type = DestinationFile

        # elif keyword == "airplane":
        #     file_type = AirplaneFile

        # elif keyword == "worktrip":
        #     file_type = WorkTripFile

        # else:
        #     return f"There is no such object type as {keyword}. Change keyword - should be string."

        save_obj = file_type(data_to_append=object_instance)
        save_obj.start()


    #Example: change_object_in_DB(employee,emp1,ssn,emp1_ssn)
    def change_object_in_DB(self,keyword,object_instance,object_id):
        '''Changes information about object in Database. \n
                keyword: employee, destination, airplane, worktrip \n
        '''

        new_file = EmployeeFile(fieldname="id",searchparam=object_id) #Looks for ssn in EmployeeFile and returns line number
        line_number = new_file.start()

        update_line = EmployeeFile(line_to_replace=line_number,replace_with=object_instance)
        update_line.start()


    def get_updated_list_from_DB(self,keyword):
        '''Returns updated list from database \n
            keyword: employee, airplane, destionation or worktrip
            '''
        if keyword == "employee":
            new_instance = EmployeeFile()               #create new instance of employee
        elif keyword == "worktrip":
            new_instance = WorkTripFile()               #create new instance of worktrip
        elif keyword == "destination":
            new_instance = DestinationFile()               #create new instance of destionation           
        elif keyword == "airplane":
            new_instance = AirplaneFile()               #create new instance of airplane

        updated_list = new_instance.start() 
        new_list = []
        for x in updated_list:
            new_list.append(x.split(','))

        return new_list