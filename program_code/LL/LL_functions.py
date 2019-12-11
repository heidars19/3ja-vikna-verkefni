from DB.DATA_API import *
from datetime import datetime
from datetime import timedelta


class LL_functions():
    '''
    
    '''
    
    data_api = DATA_API()
    
    #Call this function from EmployeeLL,DestionationLL,... Example: save_object_to_DB("employee", str(emp))
    def save_object_to_DB(self, keyword,comma_seperated_string_to_save):
        '''
        Saves a new line to database. 
        Returns True if operation successful. \n
        keyword: 'employee','airplane','destination' or 'worktrip' 
        '''
        self.data_api.set_data(keyword, data_to_append=comma_seperated_string_to_save)
        return_value = self.data_api.start()
        
        return return_value


    def change_object_in_DB(self, keyword, new_string, string_id):
        '''
        Changes a line in the database with the given 'id'. \n
        keyword: 'employee', 'destination', 'airplane', 'worktrip', 'worktripold' 
        '''
        self.data_api.set_data(keyword, fieldname="id",searchparam=string_id) #looks for id and returns line number
        line_number = self.data_api.start()

        self.data_api.set_data(keyword, line_to_replace=line_number,replace_with=new_string)
        return_value = self.data_api.start()

        return return_value


    def get_updated_list_from_DB(self,keyword):
        '''
        Returns a new list from database \n
        keyword: 'employee', 'airplane', 'destionation', 'worktrip', 'worktripold' 
        '''
        self.data_api.set_data(keyword)

        updated_list = self.data_api.start()
        new_list = []
        for i in updated_list:
            new_list.append(i.split(','))
        return new_list
    
    # def get_filtered_list_from_DB(self, keyword='destination', index_list=['id','destination']) :
    #     '''
    #     Gives a filtered list from DB.\n
    #     Keyword: employee, airplane, destionation or worktrip\n
    #     index_list needs to be a list of header columns, in the format ['id','destination']
    #     '''
    #     db_items = new_instance.get_list('destination')
    #     index_list = new_instance.find_index_from_header( 'destination', ['id','destination'])
    #     return_value = new_instance.filter_by_header_index( index_list, db_items)
    #     return return_value


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
        """
        Gets a list from database and filters out desired lines.\
        Keyword = 'employee','worktrip', 'airplane' or 'destination' \n
        index_list needs to be a list of header columns, in the format ['id','destination'] \n
        searchparam = parameter to look for in row\n
        exact_match = False will compare partial strings \n
        """
        self.data_api.set_data(keyword)
        get_list = self.data_api.start() 

        filtered_list = []
        for line in get_list[1:]:
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
    
    
    def get_available_planes(self, date_time, dest_id):
        '''
        Returns a list of available planes, given time of departure(date_time) and destination id (dest_id).\n
        date_time format: '2019-12-9 14:35" - so seconds
        '''        
        destination_list_from_db = self.get_updated_list_from_DB('destination')
        index_list = self.find_index_from_header('destination',['flight_time'])

        # Get flight time duration of planned worktrip
        result = self.get_line_from_list(destination_list_from_db, dest_id, index_list) # Filters out values from a specific line
        flight_time = result[0]
        temp_list = flight_time.split(':')
        
        start_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        end_time = self.calc_round_trip_arrival_time(flight_time, date_time, 2) # Plane is busy 1 exrta hour after landing home


        temp_airplane_list = self.get_updated_list_from_DB('airplane')
        temp_airplane_list.pop(0)
        
        airplane_list_from_db = self.filter_by_header_index([0,2],temp_airplane_list )
        worktrip_list_from_db = self.get_updated_list_from_DB('worktrip')
        worktrip_list_from_db.pop(0)
        
        
        unavailable_planes = []
        for line in worktrip_list_from_db:
            if len(line[5]) < 17: # Adding seconds cause Database files had miscellaneous format...
                line[5] += ':00'
            if len(line[6]) < 17:
                line[6] += ':00'

            if datetime.strptime(line[5], "%Y-%m-%d %H:%M:%S") < start_time and (datetime.strptime(line[6], "%Y-%m-%d %H:%M:%S") - timedelta(hours=1)) < start_time or datetime.strptime(line[5], "%Y-%m-%d %H:%M:%S") > end_time and (datetime.strptime(line[6], "%Y-%m-%d %H:%M:%S") - timedelta(hours=1)) > end_time :
                unavailable_planes.append(line[7]) # Airplanes in worktrips with overlapping time to yours

        available_planes = []
        for line in airplane_list_from_db:
            if line[0] not in unavailable_planes:
                available_planes.append(line)

        return available_planes
            

                



                
#Fall sem fær inn 1 destination og gefur id á því 