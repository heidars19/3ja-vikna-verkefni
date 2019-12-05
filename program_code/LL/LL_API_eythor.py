from LL.EmployeeLL import *
#from EmployeeLL import *
#from DB.DATA_API import * eigum ekki að tala beint við db
# from Airplanes import *
# from AirplanesLL import *
# from Destination import *
# from DestinationLL import *
 
class LL_API_eythor:

    def create(self,data_type,data_info):    #create("employee",(ssn,name,address,mobile,email,role,rank,licence))
        '''Creates new item and saves to Database. \n
        \n Returns True if operation successful.
        
        data_type: employee,airplane,destination or worktrip
        \n
        data_info: user input for corresponding item
        '''

        if data_type == 'employee':
            #ssn,name,address,mobile,email,role,rank,licence = data_info
            cr_emp = EmployeeLL()
            cr_emp.create_employee(data_info)
            #cr_emp.create_employee(ssn,name,address,mobile,email,role,rank,licence)

        # if data_type == 'airplane':

        #     airplane_id,plane_type,manufacturer,model,name,capacity = data_info

        #     cr_air == AirplaneLL()
        #     cr_emp.create_airplane(planeID,planeType,manufacturer,model,name,capacity)

        # if data_type == 'destination':

        #     destination,country,flight_time,distance,contact,emerg_number,airport = data_info

        #     cr_dest == DestinationLL()
        #     cr_dest.create_destination(destination,country,flight_time,distance,contact,emerg_number,airport)

        # if data_type =='worktrip':

        #     departing_from, arriving_at, airplane_id, departure, arrival = data_info
        #     #þarf að útfæra betur hvernig við höndlum dates og skilum niður

        #     cr_trip == WorktripLL()
        #     cr_trip.create_worktrip(departing_from, arriving_at, airplane_id, departure, arrival)   

    def change(self,data_type,data_info):
        
        #ssn,name,address,mobile,email,role,rank,licence,registration_date = data_info

        if data_type == 'employee':
            ch_emp == EmployeeLL()
            #ch_emp.change_employee(ssn,name,address,mobile,email,role,rank,licence,registration_date)
            ch_emp.change_employee(data_info)


#Staff functions
#----------------------------------------------------------------------------------------------
# def create_employee(ssn,name,address,mobile,email,role,rank,licence):
#     """Creates a new employee, returns updated list of employees."""      
    
#     new_emp = Employee(ssn,name,address,mobile,email,role,rank,licence)
#     new_emp.save_employee()
#     # updated_list = new_emp.get_employee_list()
#     # return updated_list
    
# def change_employee(ssn,name,address,mobile,email,role,rank,licence,registration_date):
#     """Changes information about employee, except ssn, name or creation date."""

#     changed_emp = Employee(ssn,name,address,mobile,email,role,rank,licence,registration_date)
#     changed_emp.change_employee()
#     #updated_list = Employee.get_employee_list
#     #return updated_list



# def main():
# #new_emp = '2501952149,Eyþór Óli Borgþórsson,Þingás 31,8453474,eythoroli95@gmail.com,Pilot,Copilot,Fokker232'
#     emp = create_employee("2501952149","Eyþór Óli Borgþórsson","Þingás 31","8453474","eythoroli95@gmail.com","Pilot","Copilot","Fokker232")

#     print(emp)
#     return
  #  new_emp = '2501952149','Eyþór Óli Borgþórsson','Þingás 31','8453474','eythoroli95@gmail.com','Pilot','Copilot','Fokker232'
  # 
  
def main():
    create_employee('2501952149','Eyþór Óli Borgþórsson','Þingás 31','8453474','eythoroli95@gmail.com','Pilot','Copilot','Fokker232')
    return

if __name__ == "__main__":
    main()
