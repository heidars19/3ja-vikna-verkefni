from LL.LL_API_eythor import *
from LL.EmployeeLL import *
from LL.Employee import *

def main():

  #-----------------------------KEYRSLUTEST------------------------------"
  # "
  #  new_emp = '2501952149','Eyþór Óli Borgþórsson','Þingás 31','8453474','eythoroli95@gmail.com','Pilot','Copilot','Fokker232'
    #create_employee('1008953349','Sigurgeir Jónasson','Þingás 31','8453474','eythoroli95@gmail.com','Pilot','Copilot','Fokker232')
    
    #change_employee('1008953349','Eyþór Óli Borgþórsson','Brunahani 31','8453474','kroli95@gmail.com','Pilot','Copilot','Fokker232','2019-12-05 17:27:37.492230')  
    new_emp = LL_API_eythor()
    new_emp.create("employee",('4455668855','Anna Jónsson','Sigurbrunnur 31','8453474','eythoroli95@gmail.com','Pilot','Copilot','Fokker232'))
    return



# staff1 = Employee('2501952149','Eyþór Óli Borgþórsson','Þingás 31','8453474','eythoroli95@gmail.com', 'Pilot', 'Copilot', 'Fokker232')
# print(staff1)

# #Prófum að stofna starfsmann
# staff1 = Employee('2501952149','Eyþór Óli Borgþórsson','Þingás 31','8453474','eythoroli95@gmail.com', 'Pilot', 'Copilot', 'Fokker232')
# print(staff1)
# #Breytum nafninu á starfsmanninum
# staff1.name = "Sigurgeir"
# print(staff1.name)

# #Prófum að búa til streng sem inniheldur persónuupplýsingar
# emp_string = '2501952149,Eyþór Óli Borgþórsson,Þingás 31,8453474,eythoroli95@gmail.com,Pilot,Copilot,Fokker232'

# new_emp = Employee.from_string(emp_string)
# print(new_emp)



if __name__ == "__main__":
    main()