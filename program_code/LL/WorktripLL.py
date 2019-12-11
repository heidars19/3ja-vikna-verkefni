from LL.Worktrip import *
from DB.DATA_API import *
from LL.LL_functions import *
import string
import datetime
from datetime import timedelta

class WorktripLL(LL_functions):

    FLUGFELAG = 'NA' # Fyrir flugnúmer
    



    def calculate_worktrip_list(self, dest_id, departure_time, aircraft_id):

        departing_from = 'Keflavík'

        index_list = self.find_index_from_header('destination',['flight_time','destination_code'])
        destination_list = self.get_updated_list_from_DB("destination")

        result = self.get_line_from_list(destination_list, dest_id, index_list) # Filters out values from a specific line
        flight_time, destination_code = tuple(result)
        # print(destination_code)
    
        arrival_time = self.calc_arrival_time(flight_time, departure_time)
        arrival_time = datetime.datetime.strftime(arrival_time,"%Y-%m-%d %H:%M" )

        other_flights_same_day = self.get_flightnumber(destination_code, departure_time)

        temp_worktrip_string = ['','', '', departing_from, dest_id, departure_time, arrival_time, aircraft_id]

        other_flights_same_day.append(temp_worktrip_string) # Add current worktrip to the list from DB

        index_list = self.find_index_from_header('worktrip',['departure'])
        total_flights_list = sorted(other_flights_same_day, key = lambda x: x[index_list[0]]) 

        final_list_of_flights = self.add_flightnumbers(total_flights_list, destination_code)

        # final_worktrip_string = ['','flight_number_out', 'flight_number_home', departing_from, dest_id, departure_time, arrival_time, aircraft_id]

        return final_list_of_flights



    def add_flightnumbers (self, work_list, destination_code) :
        '''  
        Final process of flight codes. Injects them into worktrip list.
        '''
        result_list = []
        f_number = 0

        for i, element in enumerate(work_list) :
            flight_id_out = self.FLUGFELAG + destination_code + str(f_number)
            flight_id_home = self.FLUGFELAG + destination_code + str(f_number+1)
            f_number += 2
            element[1] = flight_id_out
            element[2] = flight_id_home
            result_list.append(tuple(element))

        return result_list

        

    def get_flightnumber(self, destination_code, departure_time) :
        '''  
        Registers a worktrip and calculates the flight number. Re-arranges previous flight-numbers\n
        if needed    
        '''

        worktrip_full_list = []
        worktrip_full_list = self.get_updated_list_from_DB("worktrip")   # Get a list

        index_list = self.find_index_from_header('worktrip', ['departure', 'destination_code'])
        check_time = departure_time.split(' ') # Fá bara dags
        filtered_list = self.get_filtered_list_from_DB('worktrip', index_list, check_time[0], match=False)

        temp_list = []
        for line in filtered_list:
            temp_list.append(line.split(','))
        return temp_list
        
                    


    def create_worktrip(self,worktrip_identity):
        """
        Creates a new worktrip and saves to database. \n
        worktrip_identity = (id,flight_number_out,flight_number_home,departing_from,arriving_at,departure,arrival,\
            aircraft_id,captain,copilot,fsm,fa1,fa2,staffing_status,destination_code,registration_date)
        """
        # Need this from TUI - destination_id,date,aircraft_id
        # arriving_at,departure,aircraft_id

        worktrip_list = self.calculate_worktrip_list(*worktrip_identity)
 
        for element in worktrip_list:
            if element[0] == '' : 
                new_worktrip = Worktrip(*element)
                registration_str = new_worktrip.get_registration_str()

                return_value = self.save_object_to_DB("worktrip",registration_str)

            else : # Previously registered data, so we must fine line and overwrite it
                new_worktrip = Worktrip(*element)
                registration_str = new_worktrip.get_changes_registration_str()

                return_value = self.change_object_in_DB("worktrip",registration_str, element[0])
        return return_value


     
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


    def get_workschedule(self, date, _id):
        """
        Gets list with info about trips a employee is booked. Returns from where the flight is, to what location
        and when the flight is. 
        Keyword = 
        """
        keyword = 'worktrip'
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

    def search_instance(self,searchparam, field_to_search, field_to_return):
        if searchparam in field_to_search:
            print (field_to_return)
