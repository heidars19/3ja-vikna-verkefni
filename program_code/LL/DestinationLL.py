from DB.DATA_API import *
from LL.Destination import Destination
from LL.LL_functions import *

class DestinationLL(LL_functions):

    def create_destination(self,destination_identity):
        """Creates a new destination and saves to database."""     
        dest_id,destination,country,flight_time,distance,contact,emerg_number,airport = destination_identity #unpack
        new_dest = Destination(dest_id,destination,country,flight_time,distance,contact,emerg_number,airport)

        self.save_object_to_DB("destination",str(new_dest))

    #  def create_destination(self,dest_id,destination,country,flight_time,distance,contact,emerg_number,airport):
    #     new_destination = Destination(dest_id,destination,country,flight_time,distance,contact,emerg_number,airport)
    #     print (new_destination)
    #     log_destination = AirplaneFile(data_to_append=str(new_destination))
    #     log_destination.start()

    def get_destination_list(self):
        DestinatioFilehandler = DestinationFile()
        all_destinations = DestinatioFilehandler.start()
        all_destinations_list = []
        for destination in all_destinations:
            all_destinations_list.append(destination.split(','))
        return all_destinations_list

   


    def change_destination(self, new_info):
        new_id, new_destination, new_country, new_flight_time, new_distance, new_contact, new_emerg_number, new_airport = new_info
        updated_plain = Airplane(new_id, new_destination, new_country, new_flight_time, new_distance, new_contact, new_emerg_number, new_airport)
        
        line_in_db = AirplaneFile(fieldname="plane_id",searchparam=new_id)
        PlaneFilehandler = AirplaneFile(line_to_replace=line_in_db, replace_with=str(updated_plane))
        PlaneFilehandler.start()
