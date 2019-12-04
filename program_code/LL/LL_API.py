from Employee import *
from EmployeeLL import *
from DB.DATA_API import *
from Airplanes import *
from AirplanesLL import *


class LL_API():
"""    All functions UI needs to call. Calls use functions in corresponding Classes.
"""   

   #Staff functions
   #----------------------------------------------------------------------------------------------
    def create_employee(ssn,name,address,mobile,email,role,rank,licence):
"""        Creates a new employee, returns string with information about success.     """      
      
      # Newemp = Employee.from_string(new_emp)
        newemp = Employee(ssn,name,address,mobile,email,role,rank,licence)
        EmployeeLL.save_employee(newemp) 

        updatedlist = EmployeeLL.get_employee_list()
        return updatedlist


        #write new info to DB
        #biðja um update af listanum
        #Return updated list

        return newemp

    def change_employee(ssn,name,address,mobile,email,role,rank,licence):
        emptochange = Employee(ssn,name,address,mobile,email,role,rank,licence)

        old_info = AirplaneFile(fieldname="ssn",searchparam=ssn)
        line_number = old_info.run_me()


        data_string = ",".join([ssn,name,address,mobile,email,role,rank,licence])

        new_info = AirplaneFile(line_to_replace=line_number,replace_with=data_string)
        new_info.run_me()


       #----------------------------------------------------------------------------------------------

        #Airplanes

        def get_airplane_types():
            all_planes = get_all_planes()
            filtered_planes = filter_planes(all_planes, model)
            return filtered_planes

        def return_all_airplanes():
            all_planes = get_all_planes()
            return all_planes



        

    

        

    #if __name__ == "__main__":


        #main()



    #new_emp = '2501952149,Eyþór Óli Borgþórsson,Þingás 31,8453474,eythoroli95@gmail.com,Pilot,Copilot,Fokker232'
    emp = create_employee("2501952149","Eyþór Óli Borgþórsson","Þingás 31","8453474","eythoroli95@gmail.com","Pilot","Copilot","Fokker232")

    print(emp)
