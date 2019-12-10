from LL.Worktrip import *
from DB.DATA_API import *
from LL.LL_functions_sigurgeir import LL_functions
import string

class WorktripLL(LL_functions):

    def create_worktrip(self,worktrip_identity):
        """
        Creates a new worktrip and saves to database. \n
        worktrip_identity = (id,flight_number_out,flight_number_home,departing_from,arriving_at,departure,arrival,\
            aircraft_id,captain,copilot,fsm,fa1,fa2,staffing_status,destination_code,registration_date)
        """
        # Need this from TUI - destination,date,aircraft_id
        # arriving_at,departure,aircraft_id

        #worktrip_list = calculate_worktrip_list(*worktrip_identity)

        new_worktrip = Worktrip(*worktrip_list)
        registration_str = new_worktrip.get_registration_str()

        return_value = self.save_object_to_DB("worktrip",registration_str)
        return return_value


     
    def get_workschedule(self, date, _id):
        """
        Gets list with info about trips a employee is booked. Returns from where the flight is, to what location
        and when the flight is. 
        Keyword = 
        """
        keyword = worktrip
        date_list = self.create_date_list(date,7)
        


        row_names = ['departure']
        index_list = self.find_index_from_header(keyword, row_names)
        trips = []
        for a_date in date_list:
            filtered_list = []
            filtered_list = self.get_filtered_list_from_DB(keyword,index_list,a_date,match=False)
            trips.extend(filtered_list)
        
        
        staffmember_trips = []

        
        for trip in trips:    
            trip_info = trip.split(',')
            new_trip = Worktrip(*trip_info)
            staff = [new_trip.captain, new_trip.copilot, new_trip.fsm, new_trip.fa1, new_trip.fa2 ]
            
            if _id in staff:
                staffmember_trips.append([new_trip.departing_from, new_trip.arriving_at, new_trip.departure])
        
        return staffmember_trips
        
        
        
            

        # row_names = ['arriving_at', 'captain' ,'copilot' ,'fsm' ,'fa1' ,'fa2']
        # staff_index_list = self.find_index_from_header(keyword, row_names)
        # destination_staffmember_list = self.filter_by_header_index(staff_index_list, filtered_list)
#        return filtered_list


    def get_emp_dest_date(self, keyword,date):
        """
        Gets list of employees enrolled in a worktrip at specified date, and the destinations.\n
        Date format: YYYY-MM-DD
        """

        row_names = ['departure','arrival']
        index_list = self.find_index_from_header(keyword, row_names)
        filtered_list = self.get_filtered_list_from_DB(keyword,index_list,date,match=False)

        row_names = ['arriving_at', 'captain' ,'copilot' ,'fsm' ,'fa1' ,'fa2']
        staff_index_list = self.find_index_from_header(keyword, row_names)
        destination_staffmember_list = self.filter_by_header_index(staff_index_list, filtered_list)
        return destination_staffmember_list
           
#--------------------------------------------------------------------------


#     def calculate_worktrip_list(self, arriving_at, departure, aircraft_id):
#         # flight_number_out,flight_number_home,departing_from,departure,arrival,\
#         # ,captain,copilot,fsm,fa1,fa2,staffing_status

#         # arriving_at,destination_code,aircraft_id

#         # Get destination code and destination, also flight_time to calculate arrival time
#         # id,destination,country,flight_time,distance,contact,emerg_number,airport,destination_code,registration_date
#         index_list = self.find_index_from_header('destionation',['destination_code','flight_time'])
#         destination_list = self.get_updated_list_from_DB("Destination")

#         dest_code, flight_time = self.get_line_from_list(destination_list, aircraft_id, index_list) # Filters out values from a specific line
        
        
#         filtered_list = self.get_filtered_list_from_DB("worktrip",index_list,date)

#         self.filter_by_header_index(staff_index_list, filtered_list)

# #   "worktrip"

        
#         # # destination_code   
#         # destination_list = get_updated_list_from_DB("Destination")     #  Gets list from database
#         # destination_code = process_list(destination_list, destination_id, self.DEST_CODE_INDEX)   # Gets destination_code from a list   


#         return


#     # Constants representing index in worktrip list
#     FLUGFELAG = "NA"
#     DEST_CODE_INDEX = 0
#     DEST_ID_INDEX = 0
#     WORKTRIP_DATE_INDEX = 0
#     FLIGHT_ID_OUT = 0
#     FLIGHT_ID_HOME = 0


#     def add_flightnumbers (self, destination_code, work_list) :
#         '''  
#         Final process of flight codes. Injects them into worktrip list,\n
#         then writes lines into database.
#         '''
#         result_list = []
#         for i, element in enumerate(work_list, step=2) :
#             flight_id_out = self.FLUGFELAG + destination_code + str(i)
#             flight_id_home = self.FLUGFELAG + destination_code + str(i+1)
#             element[self.FLIGHT_ID_OUT] = flight_id_out
#             element[self.FLIGHT_ID_HOME] = flight_id_home
#             if int(element[0]) > 0 : # Overwrite lines in database
#                 new_instance = WorkTripFileOld(fieldname="id", searchparam=element[0])
#                 line_number = new_instance.start()
#                 new_instance = WorkTripFileOld(line_to_replace=line_number, replace_with=element)
#                 line_number = new_instance.start()
#             else :  # Append a new line into database
#                 new_instance = WorkTripFileOld(data_to_append=element)
#                 line_number = new_instance.start()


#     def process_list_by_index(self, working_list, data_filter, element_index) :
#         ''' 
#         Collects elements of a list with where 'data_filter' corresponds to 'element_index'\n
#         Returns a list
#         '''
#         new_list = []
#         for element in working_list :
#             if data_filter == element[element_index] :
#                 new_list.append(element)
#         return new_list

        
#     def process_list(self, incoming_list, id_num='0', index_to_return='0'):
#         ''' 
#         Finds an element of a list with id == 'id_num'\n
#         Returns a list
#         ''' 
#         for element in incoming_list:
#             if element[0] == id_num :
#                 return element[index_to_return]   # When id is found, return the value at given index 
#         return 0 # Didn't find, or error
        

#     def get_flightnumber(self, worktrip) :
#         '''  
#         Registers a worktrip and calculates the flight number. Re-arranges previous flight-numbers\n
#         if needed    
#         '''
#         destination_id = worktrip[self.DEST_ID_INDEX] 
#         worktrip_date = worktrip[self.WORKTRIP_DATE_INDEX] 


        
#         # destination_code   
#         destination_list = get_updated_list_from_DB("Destination")     #  Gets list from database
#         destination_code = process_list(destination_list, destination_id, self.DEST_CODE_INDEX)   # Gets destination_code from a list            
        
        
#         #------------------- Last number in flightnumber -----------------------------#

#         worktrip_full_list = []
#         worktrip_full_list = get_updated_list_from_DB("Worktrips")   # Get a list
#         workingy_list = process_list_by_index(worktrip_full_list, worktrip_date, self.WORKTRIP_DATE_INDEX) # Filters list by date
#         same_day_list = process_list_by_index(workingy_list, destination_id, self.DEST_ID_INDEX) # Filters list by destination
        
#         if len(self, same_day_list) == 0 :
#             worktrip_number = 0 # No other trips this day, so write directly to DB
#             new_instance = WorkTripFileOld(data_to_append=element)
#             line_number = new_instance.start()      
#         else :        
#             # More trips this day
#             same_day_list.append(worktrip) # Add current worktrip to the list from DB
            
#             work_list = sorted(same_day_list, key = lambda x: x[-1]) # Sort by last element (maybe???)
#             add_flightnumbers(destination_code, work_list)  # Processes flight number and injects them into list, write in database
#         return 
        
                    


            

