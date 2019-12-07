from DB.DATA_API import *
from LL.Destination import Destination
from LL.LL_functions import *

class DestinationLL(LL_functions):

    def create_destination(self,destination_identity):
        """Creates a new destination and saves to database."""
             
        new_dest = Destination(*destination_identity,registration_date='')
        registration_str = new_dest.get_registration_str()
        print(registration_str)
        save = self.save_object_to_DB("destination",registration_str)
        return save


    def change_destination(self, new_info):
        new_id, new_destination, new_country, new_flight_time, new_distance, new_contact, new_emerg_number, new_airport = new_info
        updated_plain = Airplane(new_id, new_destination, new_country, new_flight_time, new_distance, new_contact, new_emerg_number, new_airport)
        
        line_in_db = AirplaneFile(fieldname="plane_id",searchparam=new_id)
        PlaneFilehandler = AirplaneFile(line_to_replace=line_in_db, replace_with=str(updated_plane))
        PlaneFilehandler.start()