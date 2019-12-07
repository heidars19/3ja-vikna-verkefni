from LL.LL_API_eythor import *
from LL.EmployeeLL import *
from LL.Employee import *
from LL.LL_API import *


def main():

  #-----------------------------KEYRSLUTEST------------------------------"
 
  #CREATE
  new_instance = LL_API()
  # return_value = new_instance.create("employee",('','5665552222','Lára','Irmagata 31','0934958','lara@gmail.com','Pilot','Copilot','Airmax'))
  #return_value = new_instance.create("destination", ('','Vancouver', 'Canada','6:30:10','2.100',' John Philips','0219933884','BC_airport'))
  #return_value = new_instance.create("airplane", ('',"TF-TEST","NANTES146","Fokker","555","Skvis"))
    
  #CHANGE
  new_instance = LL_API()
  return_value = new_instance.change("employee",('21','5665552222','Breytt_Lára','Irmagata 31','0934958','lara@gmail.com','Pilot','Copilot','Airmax','2019-12-07 19:53:33.572752')

  # new_instance = LL_API()
  # return_value = new_instance.change("employee",('','5665552222','Breytt_Lára','Irmagata 31','0934958','lara@gmail.com','Pilot','Copilot','Airmax','2019-12-07 19:53:33.572752')

  return
if __name__ == "__main__":
    main()