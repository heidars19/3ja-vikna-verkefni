class Airplane():
    def __init__(self, _id, plane_id, plane_type, manufacturer, model, name, registration_date='') :
        self._id = _id
        self.planeID = plane_id
        self.planeType = plane_type
        self.manufacturer = manufacturer 	
        self.model = model
        self.name = name
        self.registration_date = registration_date

    def __repr__(self):
        return f'Airplane({_id},{self.plane_id},{self.plane_type},{self.manufacturer},{self.model,{self.name},{self.registration_date})'

    def __str__(self):
        return f'{_id},{self.plane_id},{self.plane_type},{self.manufacturer},{self.model,{self.name},{self.registration_date}'



        #====================================Functions==========================================#


