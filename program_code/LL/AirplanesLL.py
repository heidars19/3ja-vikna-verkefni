from LL_Models.Airplanes import Airplanes
from DB.DATA_API import DATA_API
from LL.LL_functions import LL_functions
import string
from datetime import datetime
from datetime import timedelta

class AirplanesLL(LL_functions):

    def create_airplane(self,airplane_identity):
        """
        Creates new instance of airplane and saves to database. \n
        airplane_identity = ('',plane_id, plane_type, manufacturer,capacity,name)\n
        """
        new_plane = Airplanes(*airplane_identity)
        registration_str = new_plane.get_registration_str() #get string with registration attributes
        save_process = self.save_object_to_DB("airplane",registration_str)

        return save_process 

    def change_airplane(self, changed_identity):
        """
        Changes information about airplane, except id or registration date. \n
        changed_identity = (id,plane_id, plane_type, manufacturer,capacity,name,registration_date)
        """

        changed_plane = Airplanes(*changed_identity)
        changed_str = changed_plane.get_changes_registration_str() #get string with all attributes
        change_process = self.change_object_in_DB("airplane", changed_str, changed_plane._id) #_id so next function can find line to overwrite with changes

        return change_process

    def get_plane_licence(self):
        """
        Returns list of plane types representing licences.
        """
        row_names = ['plane_type']
        index_list = self.find_index_from_header('airplane', row_names) 
        
        list_from_db = self.get_filtered_list_from_DB('airplane',index_list, exact_match = False, return_column=True)
        filtered_list = []
        for value in list_from_db :
            if value not in filtered_list:
                filtered_list.append(value)
        filtered_list.pop(0)
        
        return filtered_list

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
        date_time format: '2019-12-9 14:35' - so seconds
        '''        
        destination_list_from_db = self.get_updated_list_from_DB('destination')
        index_list = self.find_index_from_header('destination',['flight_time'])

        # Get flight time duration of planned worktrip
        result = self.get_line_from_list(destination_list_from_db, dest_id, index_list) # Filters out values from a specific line
        flight_time = result[0]
        
        start_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        end_time = self.calc_round_trip_arrival_time(flight_time, date_time, 2) # Plane is busy 1 extra hour after landing home

        temp_airplane_list = self.get_updated_list_from_DB('airplane')
        temp_airplane_list.pop(0)
        
        airplane_list_from_db = self.filter_by_header_index([0,2],temp_airplane_list )
        worktrip_list_from_db = self.get_updated_list_from_DB('worktrip')
        worktrip_list_from_db.pop(0)
        
            
        unavailable_planes = []
        try :
            for line in worktrip_list_from_db:
        
                if len(line[5]) < 17: # Adding seconds cause Database files had miscellaneous format...
                    line[5] += ':00'
                if len(line[6]) < 17:
                    line[6] += ':00'

                if datetime.strptime(line[5], "%Y-%m-%d %H:%M:%S") < start_time and (datetime.strptime(line[6], "%Y-%m-%d %H:%M:%S") - timedelta(hours=1)) > start_time or datetime.strptime(line[5], "%Y-%m-%d %H:%M:%S") < end_time and (datetime.strptime(line[6], "%Y-%m-%d %H:%M:%S") - timedelta(hours=1)) > end_time :
                    unavailable_planes.append(line[7]) # Airplanes in worktrips with overlapping time to yours
        except:
            pass

        available_planes = []
        for line in airplane_list_from_db:
            if line[0] not in unavailable_planes:
                available_planes.append(line)

        return available_planes
            

    def find_name_by_id(self, given_id):
        '''
        Finds a corresponding name to an 'id' in the database
        '''
        class_type = Airplanes
        db_list =  self.get_updated_list_from_DB('airplane')
        db_list.pop(0)
        for line_from_db in db_list:
            instance = class_type(*line_from_db)

            if instance._id == given_id:
                return instance.plane_type
