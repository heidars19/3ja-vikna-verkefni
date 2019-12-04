class Destination():
    
    def __init__(self, destination,	country, id, flight_time, distance, contact, emergency_number):
        self.__destination	= destination
        self.country = country
        self.id	= id
        self.flight_time = flight_time
        self.distance = distance
        self.contact = contact
        self.emergency_number = emergency_number


    def __repr__(self):
        return f'Destination({self.__destination}, {self.country}, {self.id}, {self.flight_time}, {self.distance}, {self.contact}, {self.emergency_number}')


    def __str__(self):
        return f'{self.__destination},{self.country},{self.id},{self.flight_time},{self.distance},{self.contact},{self.emergency_number}'