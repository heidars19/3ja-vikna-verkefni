class Worktrip:
    """This class keeps track of NanAir Worktrips. \n
     \n
    """

    def __init__(self,_id, flight_number_out, flight_number_home,departing_from, arriving_at, departure, arrival, aircraft_id, captain = '', copilot = "", fsm = "", fa1 = "", fa2 = "",staffing_status="", registration_date = ""): 
        from datetime import date
        #today = date.today()

        self._id = _id
        self.flight_number_out = flight_number_out          #Calculated in WorktripLL
        self.flight_number_home = flight_number_home        #Calculated in worktripLL
        self.departing_from = departing_from                #Departure location
        self.arriving_at = arriving_at                      #Destination location 
        self.departure = departure                          #Departure time
        self.arrival = arrival                              #Arrival time
        self.aircraft_id = aircraft_id         
        self.captain = captain                 
        self.copilot = copilot
        self.fsm = fsm                                      #Flight service manager
        self.fa1 = fa1                                      #Flight attendant 1
        self.fa2 = fa2                                      #Flight attendant 2
        self.staffing_status = staffing_status
        self.__registration_date = registration_date


    def get_registration_str(self):
        return f'{self.flight_number_out},{self.flight_number_home},{self.departing_from},{self.arriving_at},{self.departure},{self.arrival},{self.aircraft_id},{self.captain},{self.copilot},{self.fsm},{self.fa1},{self.fa2},{self.staffing_status}'

    def get_add_employees_str(self):
        return f'{self._id},{self.flight_number_out},{self.flight_number_home},{self.departing_from},{self.arriving_at},{self.departure},{self.arrival},{self.aircraft_id},{self.captain},{self.copilot},{self.fsm},{self.fa1},{self.fa2},{self.staffing_status},{self.registration_date}'

    