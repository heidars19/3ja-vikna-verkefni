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
        '''Returns string to use when object is first registered to Database'''

        return f'{self.plane_id},{self.plane_type},{self.manufacturer},{self.model},{self.name}'

    def get_changes_registration_str(self):
        '''Returns string to use when object is changed in Database'''

        return f'{self._id},{self.plane_id},{self.plane_type},{self.manufacturer},{self.model},{self.name},{self.registration_date}'

    def search_instance(self,searchparam, field_to_search, field_to_return=''):
        '''\nTakes in searchparameter to look up in specified column. Returns value in same row, but different column\n
            searchparam [string]: Look up value\n
            field_to_search [string]: Header of look up value\n
            field_to_return [string]: Header of return value\n
            '''
       
        if searchparam in field_to_search:
            if field_to_return:
                return [field_to_return]
            else:
                return self.get_changes_registration_str()
