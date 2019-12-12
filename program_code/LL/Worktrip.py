class Worktrip:
    """
    This class keeps track of NanAir Worktrips.
    """

    def __init__(self,_id, flight_number_out, flight_number_home,departing_from, arriving_at, departure, arrival, aircraft_id, captain = '', copilot = "", fsm = "", fa1 = "", fa2 = "",staffing_status="", registration_date = ""): 

        self._id = _id
        self.flight_number_out = flight_number_out          #Calculated in WorktripLL
        self.flight_number_home = flight_number_home        #Calculated in worktripLL
        self.departing_from = departing_from                #Departure location
        self.arriving_at = arriving_at                      #Destination location 
        self.departure = departure                          #Departure time
        self.arrival = arrival                              #Calculated in WorktripLL
        self.aircraft_id = aircraft_id         
        self.captain = captain                 
        self.copilot = copilot
        self.fsm = fsm                                      #Flight service manager
        self.fa1 = fa1                                      #Flight attendant 1
        self.fa2 = fa2                                      #Flight attendant 2
        self.staffing_status = staffing_status              #Staffing_status = staffed if worktrip has employees
        self.__registration_date = registration_date


    def get_registration_str(self):
        '''Returns string to use when object is first registered to Database'''

        return f'{self.flight_number_out},{self.flight_number_home},{self.departing_from},{self.arriving_at},{self.departure},{self.arrival},{self.aircraft_id},{self.captain},{self.copilot},{self.fsm},{self.fa1},{self.fa2},{self.staffing_status}'


    def get_changes_registration_str(self):
        '''Returns string to use when object is changed in Database'''

        return f'{self._id},{self.flight_number_out},{self.flight_number_home},{self.departing_from},{self.arriving_at},{self.departure},{self.arrival},{self.aircraft_id},{self.captain},{self.copilot},{self.fsm},{self.fa1},{self.fa2},{self.staffing_status},{self.__registration_date}'


    def search_instance(self,searchparam, field_to_search, field_to_return=''):
        '''
        Takes in searchparameter to look up in specified column. Returns value in same row, but different column\n
        searchparam: [string]..., field_to_search: [string]..., field_to_return: [string]...
        '''
        if searchparam in field_to_search:
            if field_to_return:
                return [field_to_return]
            else:
                self.get_changes_registration_str()