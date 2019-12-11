from DB.DATA_API import *
from LL.Destination import Destination
from LL.LL_functions import *

class DestinationLL(LL_functions):

    def create_destination(self,destination_identity):
        """
        Creates a new destination and saves to database.\n
        destination_identity = ('',destination,country,flight_time,distance,contact,emergency_number,airport)
        """
        # new_dest = Destination(*destination_identity)
        # TypeError: __init__() missing 2 required positional arguments: 'emerg_number' and 'airport'
        new_dest = Destination(*destination_identity)
        registration_str = new_dest.get_registration_str()

        return_value = self.save_object_to_DB("destination",registration_str)
        return return_value

    def change_destination(self, changed_identity):
        """
        Changes information about destination, except id or registration date.
        changed_identity = (id,destination,country,flight_time,distance,contact,emergency_number,airport,registration_date)
        """
    
        changed_dest = Destination(*changed_identity)
        changed_str = changed_dest.get_changes_registration_str()

        return_value = self.change_object_in_DB("destination", changed_str, changed_dest._id) # Bring 'id' seperately, so next function can find line number
        return return_value

    def get_destination_id(self,destination):

        row_names = ['destination']
        index_list = self.find_index_from_header('destination',row_names)


        filtered_list = list(set(self.get_filtered_list_from_DB('destination',index_list, exact_match = True, return_column=True)
        return filtered_list