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

        return_value = self.save_object_to_DB("employee",registration_str)
        return return_value

    def change_employee(self,changed_identity):
        """
        Changes information about employee, except ssn, name or degistration date.
        changed_identity = (id,ssn,name,address,mobile,email,role,rank,licence,registration_date)
        """

        changed_emp = Employee(*changed_identity)
        changed_str = changed_emp.get_changes_registration_str()

        return_value = self.change_object_in_DB("employee", changed_str, changed_emp._id)  # Bring 'id' seperately, so next function can find line number
        return return_value

    def working_employees(self,work_trips_by_date):
        """
        Returns list of employees working on specific day, roles and destinations.
        """

        employee_list = self.get_updated_list_from_DB('employee')
        working_employees_list = []
        available_employees_list = []
        line_list = []
        total_sets = set()
        set_list = []

        work_trips_by_date = [['Köben','1','2','3','4','5'],['Stockholm','6','7','8','9','10']]

        for i,line in enumerate(work_trips_by_date):    
            # line_list.append(line.split(','))

            for line in employee_list:
                if line[0] in work_trips_by_date[i]:
                    working_employees_list.append(line[2]+','+line[6]+','+work_trips_by_date[i][0])


        for i in range(len(work_trips_by_date)):
            set_list.append(set(work_trips_by_date[i])) 
        
        total_sets = set_list[0]
        
        if len(work_trips_by_date) != 1:   
            for i in range(1,len(set_list)):
                total_sets.update(set_list[i])

        for line in employee_list:
            if line[0] not in total_sets:
                available_employees_list.append(line)

        print(working_employees_list)
        print(available_employees_list) 
                

        
        
            

        # for sets in worktrip_sets:



        # for i,line in enumerate(work_trips_by_date):    
        #     # line_list.append(line.split(','))

        #     for line in employee_list:
        #         if line[0] not in work_trips_by_date[i]:
        #             available_employees_list.append(line)
                
        
        
        # print(working_employees_list)
        # print(available_employees_list)


            # for line in employee_list:
            #     if line[0] not in work_trips_by_date[i]:

            #         available_employees_list.append(line)
 


        # for line in employee_list[1:]:
        #     emp_line_list = line.split(',')

        # for line in work_trips_by_date[1:]:    
        #     line_list = line.split(',')

            
       
        
        

       
    

        # new_instance = file_name()
        # get_list = new_instance.start() 
        # header = new_instance.get_header().split(',') #getting header list of database

        # words_list = row_names
        # index_list = []
        
        # filtered_list = [] #list of items with searchparam specified
        # trimmed_list = []  #list of items with except searchparam specified

        # for index, value in enumerate(header): #finding index of searchparam in headerlist
        #     for word in words_list:
        #         if value == word:
        #             index_list.append(index)
            

        # for line in get_list[1:]:
        #     line_list = line.split(',')
        #     for index in index_list:
                
        #         if match: #Looks for excact match
        #             if searchparam == line_list[index]:
        #                 if return_column:
        #                     filter_list.append(line_list[index])
        #                 else:                            
        #                     if line not in filtered_list:
        #                         filtered_list.append(line)
        #             # else:
        #             #     if return_column:
        #             #         trimmed_list.append(line_list[index])
        #             #     else:                            
        #             #         if line not in trimmed_list:
        #             #             trimmed_list.append(line)

        #         else:   #Checks if value contains searchparameter
        #                     if searchparam in line_list[index]:
        #                         if return_column:
        #                                 filtered_list.append(line_list[index])
        #                         else:
        #                             if line not in filtered_list:
        #                                     filtered_list.append(line) 
        #                     # else:
        #                     #     if return_column:
        #                     #             trimmed_list.append(line_list[index])
        #                     #     else:
        #                     #         if line not in trimmed_list:
            
        #                     #             trimmed_list.append(line) 
        # # if trim:
        # #     return trimmed_list
        # # else:                     










    #def __init__ (self, data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None ) :

#     def __init__(self,emp_info,new_info =None,old_info=None):

#         ssn,name,address,mobile,email,role,rank,licence = emp_info.split(',')

#         self.emp_info = emp_info
#         self.new_info = new_info
#         self.old_info = old_info
#         self.employee = Employee(ssn,name,address,mobile,email,role,rank,licence)

#     def save_employee(self,ssn,name,address,mobile,email,role,rank,licence):
#         new_emp = Employee(ssn,name,address,mobile,email,role,rank,licence )
#         log_emp = EmployeeFile(data_to_append=str(new_emp))
#         log_emp.start()

#     def get_updated_list():
#         new_emp_list = EmployeeFile()               #create new instance
#         updated_list = new_emp_list.start()      
#         return updated_list


#     def change_employee(self,old_info,new_info):
#         '''Checks if user is trying to change invalid information'''
        
#         ssn,name,address,mobile,email,role,rank,licence = new_info.split(',')

#         old_info = EmployeeFile(fieldname="ssn",searchparam=ssn)
#     pass


# def get_employee_list():
#     new_emp_list = EmployeeFile()
#     get_emp_list = new_emp_list.start()
#     #newemp_list = start.EmployeeFile()

# return get_emp_list

# def assign_worktrip(self,worktrip):
#     pass

# def write_personalinfo(self):
#     #Save information about employee to database
#     data_to_append = str(self)
#     name_of_file = "Employees"
#     return append_data_to_file(data_to_append, name_of_file, header="")
#     pass
    
# def check_ssn(self,ssn):
#     #tala við database - láta fá kennitölu og fá true eða false
#     if false:
#         write_personalinfo(self)
#     else:
#         return True
#     pass


# def append_data_to_file(self): 

#     pass

# def read_line_in_file(self, data):
#     pass

# def change_line(self,line,filename,):
#     pass

# str(newemp)
