class Worktrip:
    """This class owns NanAir Worktrips. \n
    """

    def __init__(self,departing_from, arriving_at, departure, arrival, aircraft_id, captain = '', copilot = "", fsm = "", fa1 = "", fa2 = "", registration_date = "",worktrip_id =""): 
        from datetime import date
        #today = date.today()

        self.worktrip_id = worktrip_id
        self.departing_from = departing_from   #Departure location
        self.arriving_at = arriving_at         #Destination location 
        self.departure = departure             #Departure time
        self.arrival = arrival                 #Arrival time
        self.aircraft_id = aircraft_id         
        self.captain = captain
        self.copilot = copilot
        self.fsm = fsm                         #Flight service manager
        self.fa1 = fa1
        self.fa2 = fa2
        self.__registration_date = registration_date


    def __str__(self): #Runs when using the str() method
        return f'{self.__ssn},{self.__name},{self.address},{self.mobile},{self.email},{self.role},{self.rank},{self.licence},{self.__registration_date}'

    #name getterar fyrir privat breytur
    @property 
    def ssn(self):
        return self.__ssn
    @property
    def name(self):
        return self.__name