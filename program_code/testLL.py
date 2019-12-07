from LL.LL_API_eythor import *
from LL.EmployeeLL import *
from LL.Employee import *
from LL.LL_API import *

def main():

  #-----------------------------KEYRSLUTEST------------------------------"
 
    
    # new_emp = LL_API()
    # return_value = new_emp.create("employee",('','5665552222','Siggi','ass 31','0934958','eythoroli95@gmail.com','Pilot','Copilot','Fokker232'))
    # print(return_value)
    
    new_airplane = LL_API()
    return_value = new_airplane.create("airplane", ('',"TF-TEST","NANTES146","Fokker","555","Skvis"))
    print(return_value)
    
    # new_destination = LL_API()
    # new_destination.create("destination", ('','Vancouver', 'Canada','6:30:10','2.100',' John Philips','0219933884','BC_airport') )
    # return


if __name__ == "__main__":
    main()