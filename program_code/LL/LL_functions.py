from DB.DATA_API import DATA_API
from datetime import datetime
from datetime import timedelta


class LL_functions():
    '''
    Abstract class for LL classes. Functions that talk to DB. \n
    '''
    data_api = DATA_API()
    
    def save_object_to_DB(self, keyword,comma_seperated_string_to_save):
        '''
        Saves a new line to database. 
        Returns True if operation successful. \n
        keyword: 'employee','airplane','destination' or 'worktrip' 
        '''
        self.data_api.set_data(keyword, data_to_append=comma_seperated_string_to_save)
        save = self.data_api.start()
        
        return save


    def change_object_in_DB(self, keyword, new_string, string_id):
        '''
        Changes a line in the database with the given 'id'. \n
        keyword: 'employee', 'destination', 'airplane', 'worktrip', 'worktripold' 
        '''
        self.data_api.set_data(keyword, fieldname="id",searchparam=string_id) #looks for id and returns line number
        line_number = self.data_api.start()

        self.data_api.set_data(keyword, line_to_replace=line_number,replace_with=new_string) #line to replace and new_string to replace with
        change = self.data_api.start()

        return change


    def get_updated_list_from_DB(self,keyword):
        '''
        Returns a new list from database \n
        keyword: 'employee', 'airplane', 'destination', 'worktrip' 
        '''
        self.data_api.set_data(keyword)
        updated_list = self.data_api.start()
        new_list = []
        try :
            for i in updated_list:
                new_list.append(i.split(','))
        except:
            pass
        
        return new_list
    

    def find_index_from_header(self, keyword, row_names=[]): 
        '''
        Given keyword('employee', 'airplane', 'destionation' or 'worktrip') and a list of column names, will return a list of index numbers for those columns.
        '''
        self.data_api.set_data(keyword, header=True)
        header = self.data_api.start().split(',') #getting header list of database

        words_list = row_names
        index_list = []
    
        for index, value in enumerate(header): #finding index of searchparam in headerlist
            for word in words_list:
                if value == word:
                    index_list.append(int(index))
        
        return index_list


    def get_filtered_list_from_DB(self, keyword,index_list,searchparam="",exact_match=True, return_column=False):
        '''
        Gets a list from database and filters out desired lines.\
        Keyword = 'employee','worktrip', 'airplane' or 'destination' \n
        index_list needs to be a list of header columns, in the format ['id','destination'] \n
        searchparam = parameter to look for in row\n
        exact_match = False will compare partial strings \n
        '''
        self.data_api.set_data(keyword)
        get_list = self.data_api.start() 
        filtered_list = []
        for line in get_list:
            line_list = line.split(',')
            for index in index_list:
                
                if exact_match:  
                    if searchparam == line_list[index]:
                        if return_column:
                            filtered_list.append(line_list[index])
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


    def filter_by_header_index(self, index_list, list_of_comma_seperated_strings):
        '''
        Will filter out indexed columns from a comma seperated string
        index_list = list of indexes to keep in the format [0, 4, 6]
        ''' 
        index_sorted_list = []
        for item in list_of_comma_seperated_strings:
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
        '''
        Returns a list of consecutive dates
        '''
        date_list = []
        date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
        for dates in range (int(day_to_add)):
            date_list.append(str(date_object))
            date_object += timedelta(days=step)
        
        return date_list


    def get_line_from_list(self, list_of_comma_seperated_strings, id_number, index_list) :
        '''
        List from database, id number for the line, and list of indexes for values you need\n
        Returns a list with indexed values as elements
        '''
        temp_list = []
        for line in list_of_comma_seperated_strings:
            if line[0] == id_number :
                for index in index_list :
                    temp_list.append(line[int(index)])
                return (temp_list)
        return 0 # Found nothing
    
    
    def calc_round_trip_arrival_time(self, duration, start_time, layover=1) :
        '''
        Given flight duration 1-way and departure time, will calculate when plane arrives back home.
        '''
        temp_list = duration.split(':') # temp_list[0] = hours and temp_list[1] = min, skipping seconds
        round_trip_duration = timedelta(hours=int(temp_list[0]), minutes=int(temp_list[1]))*2 + timedelta(hours=layover)
        end_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M") + round_trip_duration
        return end_time
