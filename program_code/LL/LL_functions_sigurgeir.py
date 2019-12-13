from DB.DATA_API import *
from datetime import datetime
from datetime import timedelta


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


    def find_index_from_header(self, keyword, row_names=[]):
    
        file_name = self.file_type(keyword)
        new_instance = file_name()
        header = new_instance.get_header().split(',') #getting header list of database

        words_list = row_names
        index_list = []
    
        for index, value in enumerate(header): #finding index of searchparam in headerlist
            for word in words_list:
                if value == word:
                    index_list.append(int(index))
        return index_list

    def get_filtered_list_from_DB(self, keyword,index_list,searchparam="",match=True, return_column=False):
        """
        Keyword = employee,worktrip, airplane, destination \n
        row_names = filtered word from header \n
        searchparam = parameter to look for in row\n
        match = True if looking for excact macth \n
        match = False if looking for data containing specific string \n
        """
        file_name =  self.file_type(keyword)
        new_instance = file_name()
        get_list = new_instance.start() 

        
        filtered_list = []
        for line in get_list[1:]:
            line_list = line.split(',')
            for index in index_list:
                
                if match:    #Looks for excact match
                    if searchparam == line_list[index]:
                        if return_column:
                            filter_list.append(line_list[index])
                        else:                            
                            if line not in filtered_list:
                                filtered_list.append(line)

                else:   #Checks if value contains searchparameter
                    if searchparam in line_list[index]:
                        if return_column:
                            filtered_list.append(line_list[index])
                        else:
                            if line not in filtered_list:
                                filtered_list.append(line)
        return filtered_list


    def filter_by_header_index(self, index_list, db_items):
        '''
        index_list = list of iteams that needs to be filtered from a string to a new list
        db_str_list = line from database that need to be filtered
        '''
    
        index_sorted_list = []
        for item in db_items:
            tmp_list = []
            tmp_list2 = []
            
            if type(item) == str:
                tmp_list = item.split(',')
                for index in index_list:
                    tmp_list2.append(tmp_list[index])
            
            if type(item) == list:
                for index in index_list:
                    tmp_list2.append(item[index])
            index_sorted_list.append(tmp_list2)

        return index_sorted_list


    def create_date_list(self, date_str, day_to_add, step=1):
        date_list = []
        date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
        for dates in range (int(day_to_add)):
            date_list.append(str(date_object))
            date_object += timedelta(days=step)
        return date_list
    
    def info_from_class(self, class_type, data_from_db, searchparam, field_to_search, field_to_return):
                
        for instance in data_from_db:
            instance_info = instance.split(',')
            new_instance = class_type(*instance_info)
            

            # if searchparam in field_to_search:
            #     return field_to_return
            
            # else:
            #     return False
            


    

        '''
        
date_str = '09-19-2018'

date_object = datetime.strptime(date_str, '%m-%d-%Y').date()
print(type(date_object))
print(date_object)'''




                





                



                
