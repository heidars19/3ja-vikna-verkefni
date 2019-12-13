from LL_Models.Worktrip import Worktrip
from DB.DATA_API import DATA_API
from LL.LL_functions import LL_functions
import string
from datetime import timedelta
from datetime import datetime

class WorktripLL(LL_functions):

    FLUGFELAG = 'NA' # Fyrir flugnúmer

    def create_worktrip(self,worktrip_identity):
        """
        Creates a new worktrip and saves to database. \n
        worktrip_identity = (id,flight_number_out,flight_number_home,departing_from,arriving_at,departure,arrival,
        aircraft_id,captain,copilot,fsm,fa1,fa2,staffing_status,destination_code,registration_date)
        """
        worktrip_list = self.calculate_worktrip_list(*worktrip_identity)
 
        for element in worktrip_list:
            if element[0] == '' : 
                new_worktrip = Worktrip(*element)
                registration_str = new_worktrip.get_registration_str()

                return_value = self.save_object_to_DB("worktrip",registration_str)

            else : # Previously registered data, so we must find the line and overwrite it
                new_worktrip = Worktrip(*element)
                registration_str = new_worktrip.get_changes_registration_str()

                return_value = self.change_object_in_DB("worktrip",registration_str, element[0])

        return return_value

    def add_employees_worktrip(self,worktrip_staffed):
        """
        Adds staff to worktrip.
        """
        staffed_worktrip = Worktrip(*worktrip_staffed)
        changed_str = staffed_worktrip.get_changes_registration_str()
        
        add_employees = self.change_object_in_DB("worktrip",changed_str,staffed_worktrip._id)

        return add_employees

    
    def calc_arrival_time(self, duration, start_time, layover=1):
        '''
        Given flight duration 1-way and departure time, will calculate when plane arrives back home.
        '''
        temp_list = duration.split(':') # temp_list[0] = hours and temp_list[1] = min, skipping seconds
        round_trip_duration = timedelta(hours=int(temp_list[0]), minutes=int(temp_list[1]))*2 + timedelta(hours=layover)
        end_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M") + round_trip_duration
        return end_time
        

    def calculate_worktrip_list(self, dest_id, departure_time, aircraft_id):
        '''
        Calculate values that need to go into creating a worktrip, before writing it into database.
        '''

        departing_from = 'Keflavík'

        index_list = self.find_index_from_header('destination',['flight_time','destination_code'])
        destination_list = self.get_updated_list_from_DB("destination")

        result = self.get_line_from_list(destination_list, dest_id, index_list) # Filters out values from a specific line
        flight_time, destination_code = tuple(result)
    
        arrival_time = self.calc_arrival_time(flight_time, departure_time)
        arrival_time = datetime.strftime(arrival_time,"%Y-%m-%d %H:%M" )

        other_flights_same_day = self.get_flightnumber(destination_code, departure_time)

        temp_worktrip_string = ['','', '', departing_from, dest_id, departure_time, arrival_time, aircraft_id]

        other_flights_same_day.append(temp_worktrip_string) # Add current worktrip to the list from DB

        index_list = self.find_index_from_header('worktrip',['departure'])
        total_flights_list = sorted(other_flights_same_day, key = lambda x: x[index_list[0]]) 

        final_list_of_flights = self.add_flightnumbers(total_flights_list, destination_code)

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
        Registers a worktrip and calculates the flight number. Re-arranges previous flight-numbers if needed    
        '''
        worktrip_full_list = []
        worktrip_full_list = self.get_updated_list_from_DB("worktrip")   # Get a list

        index_list = self.find_index_from_header('worktrip', ['departure', 'destination_code'])
        check_time = departure_time.split(' ') # Fá bara dags
        filtered_list = self.get_filtered_list_from_DB('worktrip', index_list, check_time[0], exact_match=False)

        temp_list = []
        for line in filtered_list:
            temp_list.append(line.split(','))
        return temp_list


    def get_emp_dest_date(self, date , include_arrivaldate=False):
        """
        Gets list of employees enrolled in a worktrip at specified date, and the destinations.\n
        Date format: YYYY-MM-DD
        """
        trips = self.get_updated_list_from_DB('worktrip')
        trips.pop(0)
        
        staffmember_trips = []
        for trip in trips: 
            new_trip = Worktrip(*trip) 
            new_trip.arrival = new_trip.arrival.split()
            new_trip.departure = new_trip.departure.split()
            if include_arrivaldate:
                if date == new_trip.departure[0] or date == new_trip.arrival[0]:
                    staffmember_trips.append([new_trip.arriving_at, [new_trip.captain, new_trip.copilot, new_trip.fsm, new_trip.fa1, new_trip.fa2 ]])
                    
            
            if not include_arrivaldate:                
                if date == new_trip.departure[0]:
                    staffmember_trips.append([new_trip.arriving_at, [new_trip.captain, new_trip.copilot, new_trip.fsm, new_trip.fa1, new_trip.fa2 ]])
        
        return staffmember_trips
    

    def get_workschedule(self, date, _id='', days=7):
        """
        Gets list with info about trips an employee is booked. Returns from where the flight is, to what location
        and when the flight is. 
        """
        keyword = 'worktrip'
        date_list = self.create_date_list(date,days)

        row_names = ['departure']
        index_list = self.find_index_from_header(keyword, row_names)
        trips = []
        for a_date in date_list:
            filtered_list = []
            filtered_list = self.get_filtered_list_from_DB(keyword,index_list,a_date,exact_match=False)
            trips.extend(filtered_list)
        
        staffmember_trips = []
    
        for trip in trips:    
            trip_info = trip.split(',')
            new_trip = Worktrip(*trip_info)
            staff = [new_trip.captain, new_trip.copilot, new_trip.fsm, new_trip.fa1, new_trip.fa2 ]
            
            if _id:
                if _id in staff:
                    staffmember_trips.append([new_trip.departing_from, new_trip.arriving_at, new_trip.departure])
            else:
                trips_list = [x.split(',') for x in trips]
                return trips_list
        return staffmember_trips
 
 
    def get_worktrips_by_date(self, date, days) :
        '''
        Returns a list of worktrips, old or new
        '''
        start_date = datetime.strptime(date, '%Y-%m-%d')
        if start_date < datetime.now() :
            worktrip_list = self.get_updated_list_from_DB('worktripold') 
        else :
            worktrip_list = self.get_updated_list_from_DB('worktrip')       
        
        end_date = start_date + timedelta(days=days)
        worktrip_list.pop(0)
        
        final_worktrip_list = []
        for line in worktrip_list:
            if len(line[5]) < 17 :
                line[5] += ':00'
            
            if datetime.strptime(line[5], '%Y-%m-%d %H:%M:%S') > start_date and datetime.strptime(line[5], '%Y-%m-%d %H:%M:%S') < end_date :
                final_worktrip_list.append(line)
        
        return final_worktrip_list
    