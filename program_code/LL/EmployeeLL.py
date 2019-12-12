from DB.DATA_API import *
from LL.Employee import *
from LL.LL_functions import *

#from DB.AirplaneFile import AirplaneFile

class EmployeeLL(LL_functions):

    def create_employee(self,personal_identity):
        """
        Creates a new employee and saves to database. \n
        personal_identity = ('',ssn,name,address,mobile,email,role,rank,licence)
        """
        new_emp = Employee(*personal_identity)
        registration_str = new_emp.get_registration_str()

        save = self.save_object_to_DB("employee",registration_str)
        return save

    def change_employee(self,changed_identity):
        """
        \nChanges information about employee, except ssn, name or degistration date.\n
        changed_identity = (id,ssn,name,address,mobile,email,role,rank,licence,registration_date)
        """

        changed_emp = Employee(*changed_identity)
        changed_str = changed_emp.get_changes_registration_str()

        change = self.change_object_in_DB("employee", changed_str, changed_emp._id)  # Bring 'id' seperately, so next function can find line number
        return change

    def working_employees(self,work_trips_by_date):
        """
        \nReturns list of employees working at specific date, their roles and destinations.\n
        work_trips_by_date [list] : list of worktrips at specified date.
        """

        employee_list = self.get_updated_list_from_DB('employee')
        working_employees_list = []
        line_list = []

        for i,line in enumerate(work_trips_by_date):   

            for line in employee_list:
                if line[0] in work_trips_by_date[i]:
                    working_employees_list.append([line[2],line[6],work_trips_by_date[i][0]])
        
        return working_employees_list


    def available_employees(self,work_trips_by_date='', role='',rank='', a_license=''):
        """
        \nReturns list of available employees - id, name role and rank.\n
            captains: rank='Captain', a_license='Airplane Type'
            copilots: role='Pilot', a_license='Airplane Type'
            Flight Attendant: rank='Flight Attendant'
            Cabin Crew: role='Cabincrew'
        """

        employee_list = self.get_updated_list_from_DB('employee')
        available_employees_list = []
        total_sets = set()
        set_list = []

        for i in range(len(work_trips_by_date)):
            set_list.append(set(work_trips_by_date[i])) 
        
        total_sets = set_list[0]
        
        if len(work_trips_by_date) != 1:   
            for i in range(1,len(set_list)):
                total_sets.update(set_list[i])

        for line in employee_list:
            if line[0] not in total_sets:
                available_employees_list.append(line)
               
        qualified_staff = []
        for instance in available_employees_list:
            instance = Employee(*instance)
            if rank: 
                check_staff = instance.search_instance(rank, instance.rank)
                if check_staff:
                    if a_license:
                        check_staff = instance.search_instance(a_license, instance.licence)
                        if check_staff:
                            qualified_staff.append(check_staff.split(','))
                    else:
                        qualified_staff.append(check_staff.split(','))
            elif role:
                check_staff = instance.search_instance(role, instance.role)
                if check_staff:
                    if a_license:
                        check_staff = instance.search_instance(a_license, instance.licence)
                        if check_staff:
                            qualified_staff.append(check_staff.split(','))
                    else:
                        qualified_staff.append(check_staff.split(','))
        return qualified_staff


    def find_pilot_with_license(self, a_licence):
        pilot_list = []
        employee_list = self.get_updated_list_from_DB('employee')
        
        for instance in employee_list:
            instance = Employee(*instance)
            if a_licence:
                check_staff = instance.search_instance(a_licence, instance.licence)
                if check_staff:
                    pilot_list.append(check_staff.split(','))
        
        return pilot_list




    def find_name_by_id(self, given_id):
            if given_id:
                class_type = Employee
                airplane_list =  self.get_updated_list_from_DB('employee')
                airplane_list.pop(0)
                for line_from_db in airplane_list:
                    instance = class_type(*line_from_db)

                    if instance._id == given_id:
                        return instance.name
            else:
                return given_id
