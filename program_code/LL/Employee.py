from DB.DATA_API import *

class Employee:
    """This class represents the Employees of Nan Air and keeps track of their information."""

    def __init__(self,_id,ssn,name,address,mobile,email,role,rank,licence,registration_date=""): 
        from datetime import date
        #today = date.today()

        self._id = _id
        self.ssn = ssn
        self.name = name
        self.address = address
        self.mobile = mobile
        self.email = email
        self.role = role
        self.rank = rank
        self.licence = licence
        self.__registration_date = registration_date


    def __repr__(self):
        return f'Employee({self.ssn},{self.name},{self.address},{self.mobile},{self.email},{self.role},{self.rank},{self.licence})'

    def get_registration_str(self):
        '''Returns string to use when object is first registered to Database'''
        return f'{self.ssn},{self.name},{self.address},{self.mobile},{self.email},{self.role},{self.rank},{self.licence}'

    def get_changes_registration_str(self):
        '''Returns string to use when object is changed in Database'''

        return f'{self._id},{self.ssn},{self.name},{self.address},{self.mobile},{self.email},{self.role},{self.rank},{self.licence},{self.__registration_date}'

    def search_instance(self,searchparam, field_to_search, field_to_return=''):
        '''\nTakes in searchparameter to look up in specified column. Returns value in same row, but different column\n
            searchparam [string]: Look up value\n
            field_to_search [string]: Header of look up value\n
            field_to_return [string]: Header of return value\n
            '''
        if type(searchparam) == list:
            if searchparam in field_to_search:
                if field_to_return:
                    return [field_to_return]
                else:
                    self.get_changes_registration_str()
        else:
            if searchparam == field_to_search:
                if field_to_return:
                    return [field_to_return]
                else:
                    self.get_changes_registration_str()