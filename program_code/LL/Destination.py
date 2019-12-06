class Destination():

    def __init__(self, id, destination,	country,  flight_time, distance, contact, emerg_number, airport):
        self.id	= id
        self.destination = destination
        self.country = country
        self.flight_time = flight_time
        self.distance = distance
        self.contact = contact
        self.emergency_number = emerg_number
        self.airport = airport


    def __repr__(self):
        return f'Destination({self.destination},{self.country},,{self.flight_time},{self.distance},{self.contact},{self.emergency_number}'


    def __str__(self):
        return f'{self.id},{self.destination},{self.country},{self.id},{self.flight_time},{self.distance},{self.contact},{self.emergency_number}'

    def __db__(self):
        return f'{self.destination},{self.country},{self.flight_time},{self.distance},{self.contact},{self.emergency_number},{self.airport}'
