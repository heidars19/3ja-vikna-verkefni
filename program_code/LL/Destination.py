class Destination():

    def __init__(self, _id, destination, country, flight_time, distance, contact, emerg_number, airport, registration_date=''):
        self._id = _id
        self.destination = destination
        self.country = country
        self.flight_time = flight_time
        self.distance = distance
        self.contact = contact
        self.emergency_number = emerg_number
        self.airport = airport
        self.registration_date = registration_date


    def __repr__(self):
        return f'Destination({self.destination},{self.country},{self.flight_time},{self.distance},{self.contact},{self.emergency_number},{self.airport}'

    def registration(self):
        return f'{self.destination},{self.country},{self.flight_time},{self.distance},{self.contact},{self.emergency_number},{self.airport}'

    def change_registration(self):
        f'{self._id},{self.destination},{self.country},{self.flight_time},{self.distance},{self.contact},{self.emergency_number},{self.airport},{self.registration_date}'



