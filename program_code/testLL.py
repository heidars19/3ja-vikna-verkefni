from LL.LL_API_eythor import *
from LL.EmployeeLL import *
from LL.Employee import *
from LL.LL_API import *



def return_msg(msg, keyword):
  if msg == 1:
    print("Success in {}".format(keyword))
  elif msg == 0 :
    print("No success in {}".format(keyword))
  elif msg == -1 :
    print("An unknow error occurred while {}".format(keyword))
  elif msg == -404 :
    print("File not Found error on {}".format(keyword))   
  else:
    print("An unknow error occurred or not getting return value from DB")
  return

def main():

  #-----------------------------KEYRSLUTEST------------------------------"
 
  #CREATE
  # new_instance = LL_API()
  # return_value = new_instance.create("employee",('','5665552222','Glæný Lára','Irmagata 31','0934958','lara@gmail.com','Pilot','Copilot','Airmax'))
  # return_value = new_instance.create("destination", ('','Vancouver', 'Canada','6:30:10','2.100','John Philips','0219933884','BC_airport'))
  # return_value = new_instance.create("airplane", ('',"TF-TEST","NANTES146","Fokker","555","Skvis"))
  # return_msg(return_value, f"creating a new destination, code:{return_value}")

  #CHANGE
  
  # new_instance = LL_API()
  # return_value = new_instance.change("destination",('13','Milano', 'Italy','6:30:10','2.100','John Philips','0219933884','BC_airport','2019-12-07 21:39:33.300255'))
  # return_value = new_instance.change("employee",('23','2001933874', 'Gömul Lára','Bústaðarvegi 6','8922773','gamla@geit.org','Pilot','Captain','F1Fighters','2019-12-08 12:46:12.455312'))
  # return_value = new_instance.change("airplane",('56','TF-EOC', 'NAFokker80','Fokker','F800','Heiðar er Bestur','2019-12-07 20:18:43.536857'))
  # return_value = new_instance.change("worktrip",('13','Milano', 'Italy','6:30:10','2.100','John Philips','0219933884','BC_airport','2019-12-07 21:39:33.300255'))
  # return_msg(return_value, f"changing, code:{return_value}")

  #GET_LIST
  
  # new_instance = LL_API()
  # new_list = new_instance.get_list('employee')
  # new_list = new_instance.get_list('airplane')
  # new_list = new_instance.get_list('destination')
  print(new_list)

  return



  
if __name__ == "__main__":
    main()