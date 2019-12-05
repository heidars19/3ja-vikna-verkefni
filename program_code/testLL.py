from LL.LL_API_eythor import *
from LL.Employee import *

def main():
  #  new_emp = '2501952149','Eyþór Óli Borgþórsson','Þingás 31','8453474','eythoroli95@gmail.com','Pilot','Copilot','Fokker232'
    LL_API_eythor.create_employee('2501952149','Eyþór Óli Borgþórsson','Þingás 31','8453474','eythoroli95@gmail.com','Pilot','Copilot','Fokker232')

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


#     return 
# if __name__ == "__main__":
#     main()