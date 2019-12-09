class Airplanes():
<<<<<<< HEAD
    def __init__(self, _id,plane_id, plane_type, manufacturer, capacity, name, registration_date=''):
=======
    def __init__(self, _id,plane_id, plane_type, manufacturer, model, name, registration_date=''):
>>>>>>> 58c6b1e86f888904861e8c2261581a5bdb53063f
        self._id = _id
        self.plane_id = plane_id
        self.plane_type = plane_type
        self.manufacturer = manufacturer 	
<<<<<<< HEAD
        self.capacity = capacity
=======
        self.model = model
>>>>>>> 58c6b1e86f888904861e8c2261581a5bdb53063f
        self.name = name
        self.registration_date = registration_date

    def __repr__(self):
<<<<<<< HEAD
        return f'Airplanes({self._id},{self.plane_id},{self.plane_type},{self.manufacturer},{self.capacity},{self.name},{self.registration_date})'

    def get_registration_str(self):
        return f'{self.plane_id},{self.plane_type},{self.manufacturer},{self.capacity},{self.name}'

    def get_changes_registration_str(self):
        return f'{self._id},{self.plane_id},{self.plane_type},{self.manufacturer},{self.capacity},{self.name},{self.registration_date}'
=======
        return f'Airplanes({self._id},{self.plane_id},{self.plane_type},{self.manufacturer},{self.model},{self.name},{self.registration_date})'

    def get_registration_str(self):
        return f'{self.plane_id},{self.plane_type},{self.manufacturer},{self.model},{self.name}'

    def get_changes_registration_str(self):
        return f'{self._id},{self.plane_id},{self.plane_type},{self.manufacturer},{self.model},{self.name},{self.registration_date}'
>>>>>>> 58c6b1e86f888904861e8c2261581a5bdb53063f
