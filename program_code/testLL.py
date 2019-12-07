from LL.LL_API_eythor import *
from LL.EmployeeLL import *
from LL.Employee import *
from LL.LL_API import *

def main():

  #-----------------------------KEYRSLUTEST------------------------------"
 
    
    new_emp = LL_API()
    new_emp.create("employee",('','5665552222','Siggi','ass 31','0934958','eythoroli95@gmail.com','Pilot','Copilot','Fokker232'))
    
    # new_airplane = LL_API()
    # new_airplane.create("airplane", ('',"TF-TEST","NANTES146","Fokker","555","Skvis"))
    
    new_destination = LL_API()
    new_destination.create("destination", ('','Vancouver', 'Canada','6:30:10','2.100',' John Philips','0219933884','BC_airport') )
    return



if __name__ == "__main__":
    main()