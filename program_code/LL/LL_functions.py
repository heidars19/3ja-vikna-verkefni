from DB.DATA_API import *
from datetime import datetime
from datetime import timedelta


class LL_functions():
    '''
    
    '''
    
    data_api = DATA_API()
    
    #Call this function from EmployeeLL,DestionationLL,... Example: save_object_to_DB("employee", str(emp))
    def save_object_to_DB(self, keyword,object_instance):
        '''Saves new object to database. \n
        \n Returns True if operation successful.
        keyword: employee,airplane,destination or worktrip as string
        \n 
        object_instance: Instance of employee, airplane, destination or worktrip as string. 
        '''

        self.data_api.set_data(keyword, data_to_append=object_instance)

        return_value = self.data_api.start()
        
        return return_value


    def change_object_in_DB(self, keyword, new_string, string_id):
        '''
        Changes information about object in Database. \n
        keyword: employee, destination, airplane, worktrip, worktripold \n
        '''
        self.data_api.set_data(keyword, fieldname="id",searchparam=string_id) #looks for id and returns line number
        line_number = self.data_api.start()

        self.data_api.set_data(keyword, line_to_replace=line_number,replace_with=new_string)
        return_value = self.data_api.start()

        return return_value


    def get_updated_list_from_DB(self,keyword):
        '''Returns updated list from database \n
            keyword: employee, airplane, destionation or worktrip
            '''
        self.data_api.set_data(keyword)

        updated_list = self.data_api.start()
        new_list = []
        for i in updated_list:
            new_list.append(i.split(','))
        return new_list


    def find_index_from_header(self, keyword, row_names=[]): 
        self.data_api.set_data(keyword, header=True)
        header = self.data_api.start().split(',') #getting header list of database

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
        self.data_api.set_data(keyword)
        get_list = self.data_api.start() 

        
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





                



                
