class Airplanes():
    def __init__(self, _id,plane_id, plane_type, manufacturer, model, name, registration_date=''):
        self._id = _id
        self.plane_id = plane_id
        self.plane_type = plane_type
        self.manufacturer = manufacturer 	
        self.model = model
        self.name = name
        self.registration_date = registration_date

    def __repr__(self):
        return f'Airplanes({self._id},{self.plane_id},{self.plane_type},{self.manufacturer},{self.model},{self.name},{self.registration_date})'

    def get_registration_str(self):
        return f'{self.plane_id},{self.plane_type},{self.manufacturer},{self.model},{self.name}'

    def get_changes_registration_str(self):
        return f'{self._id},{self.plane_id},{self.plane_type},{self.manufacturer},{self.model},{self.name},{self.registration_date}'
