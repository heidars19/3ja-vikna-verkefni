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


    def change_object_in_DB(self, keyword, new_string, string_id):
        '''
        Changes information about object in Database. \n
        keyword: employee, destination, airplane, worktrip, worktripold \n
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

    
    def get_filtered_list_from_DB(self,keyword,row_names=[],searchparam="",match=True):
        """
        Keyword = employee,worktrip, airplane, destination \n
        row_names = filtered word from header \n
        searchparam = parameter to look for in row\n
        match = True if looking for excact macth \n
        match = False if looking for data containing specific string \n
        """

        file_name = self.file_type(keyword)

        new_instance = file_name()
        get_list = new_instance.start() 
        header = new_instance.get_header().split(',')

        words_list = row_names
        index_list = []
        
        filtered_list = []

        for index, value in enumerate(header):
            for word in words_list:
                if value == word:
                    index_list.append(index)

        if match:    #Looks for excact match
            for line in get_list[1:]:

                line_list = line.split(',')
                for index in index_list:
                    if searchparam == line_list[index]:
                        if line not in filtered_list:
                            filtered_list.append(line_list[index])

        else:   #Checks if value contains searchparameter
            for line in get_list[1:]:
                line_list = line.split(',')
                for index in index_list:
                    if searchparam in line_list[index]:
                        if line not in filtered_list:
                            filtered_list.append(line_list[index])


        return filtered_list


                    
                





                



                
