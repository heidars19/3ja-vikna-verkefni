from DB.DATA_API import DATA_API
from LL_Models.Employee import Employee
from LL.LL_functions import LL_functions


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
        Changes information about employee, except ssn, name or degistration date.\n
        changed_identity = (id,ssn,name,address,mobile,email,role,rank,licence,registration_date)
        """
        changed_emp = Employee(*changed_identity)
        changed_str = changed_emp.get_changes_registration_str()

        change = self.change_object_in_DB("employee", changed_str, changed_emp._id)  # Bring 'id' seperately, so next function can find line number
        return change


    def working_employees(self,work_trips_by_date, ):
        """
        Returns list of employees working at specific date, their roles and destinations.\n
        work_trips_by_date [list] : list of worktrips at specified date.
        """
        employee_list = self.get_updated_list_from_DB('employee')
        working_employees_list = []
        
        for dest_emp_info in work_trips_by_date:
            dest, emp_list = dest_emp_info
            for emp_instance in employee_list:
                new_emp = Employee(*emp_instance)
                if new_emp._id in emp_list:
                    working_employees_list.append([new_emp.name,  new_emp.role, dest])
        
        return working_employees_list


    def available_employees(self,staff_on_trips):
        """
        Returns list of available employees - id, name role and rank.\n
        captains: rank='Captain', a_license='Airplane Type'
        copilots: role='Pilot', a_license='Airplane Type'
        Flight Attendant: rank='Flight Attendant'
        Cabin Crew: role='Cabincrew'
        """
        employee_list = self.get_updated_list_from_DB('employee')
        employee_list.pop(0)
        all_busy_staff = []
        available_employees_list = []

        for trip_info in staff_on_trips:
            destinatin, staff_list = trip_info
            all_busy_staff.extend(staff_list)

        for employee_info in employee_list:
            new_employee = Employee(*employee_info)
            if new_employee._id not in all_busy_staff:
                available_employees_list.append(new_employee.get_changes_registration_str().split(','))
        
        return available_employees_list


    def find_qualified_staff(self, staff_list, role='', rank='', a_license='' ):
        '''
        Finds staff with required role, rank and licence. Returns a list.
        '''
        qualified_staff = []
        if role == 'all':
            return staff_list
        
        for staff_info in staff_list:
            instance = Employee(*staff_info)
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
        '''
        Returns a list with pilots with the correct licence
        '''
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
        '''
        Finds a corresponding name to an 'id' in the database
        '''
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
