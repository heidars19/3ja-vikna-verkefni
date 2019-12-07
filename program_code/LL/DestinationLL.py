from DB.DATA_API import *
from LL.Destination import Destination
from LL.LL_functions import *

class DestinationLL(LL_functions):

    def create_destination(self,destination_identity):
        """Creates a new destination and saves to database."""
             
        new_dest = Destination(*destination_identity,registration_date='')
        registration_str = new_dest.get_registration_str()

        return_value = self.save_object_to_DB("destination",registration_str)
        return return_value


    def change_destination(self, new_info):
        new_id, new_destination, new_country, new_flight_time, new_distance, new_contact, new_emerg_number, new_airport, new_reg_date = new_info
        
        new_dest = Destination(*new_info)
        registration_str = new_dest.get_changes_registration_str()
        print(registration_str)
        return_value = self.change_object_in_DB("destination", registration_str, new_id) # Bring 'id' seperately, so next function can find line number
        #print(return_value)
        return return_value
