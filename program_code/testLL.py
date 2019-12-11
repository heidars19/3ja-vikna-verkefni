from LL.LL_API import LL_API
from LL.EmployeeLL import *
from LL.Employee import *
from DB.DATA_API import *


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
 

  new_instance = LL_API()

  #CREATE

  # """Destination"""
  # return_value = new_instance.create("destination", ('','Test', 'Canada','6:30:10','2.100','John Philips','0219933884','BC_airport'))

  
  # return_value = new_instance.create("employee",('','5665552222','Eyþór Óli','Irmagata 31','0934958','lara@gmail.com','Pilot','Copilot','Airmax'))
  # return_value = new_instance.create("destination", ('','Toronto', 'Canada','6:30:10','2.100','John Philips','0219933884','BC_airport'))
  #return_value = new_instance.create("airplane", ('',"TF-Eythor","NANTES146","Fokker","555","Skvis"))
  # return_value = new_instance.create("worktrip",('','','','','15','2019-12-20 06:45:00','','5')) # dest_id, departure_time, airplane_id
  #return_msg(return_value, f"creating a new object, code:{return_value}")

  #CHANGE
  # return_value = new_instance.change("destination",('16','Milano', 'Italy','6:30:10','2.100','John Philips','0219933884','BC_airport','2019-12-08 13:41:20.362544'))
  # return_value = new_instance.change("employee",('23','2001933874', 'Gömul Lára','Bústaðarvegi 6','8922773','gamla@geit.org','Pilot','Captain','F1Fighters','2019-12-08 12:46:12.455312'))
  # return_value = new_instance.change("airplane",('73','TF-breytt', 'NAbreytt','Fokker','F800','Breytt','13:25:38.975230'))
  # return_value = new_instance.change("worktrip",('13','Milano', 'Italy','6:30:10','2.100','John Philips','0219933884','BC_airport','2019-12-07 21:39:33.300255'))
  # return_msg(return_value, f"changing, code:{return_value}")

  #GET_LIST
  
  #new_list = new_instance.get_list('employee')
  #new_list = new_instance.get_list('airplane')
  # new_list = new_instance.get_list('destination')
  # new_list = new_instance.get_list('worktrip')
  # new_list = new_instance.get_list('worktrip',"working_employees",'2019-12-20')
  # new_list = new_instance.get_list('destination',"destination_id","Vancouver")
  # new_list = new_instance.get_list('airplane','plane_licences') 
  new_list = new_instance.get_list('worktrip', 'workschedule', '2019-12-10', '11')
  #new_list  = new_instance.get_list("worktrip", "available_employees", "2019-12-20", role='Pilot', rank='', a_license='Fokker232')
  # print(new_list)
  # new_list = new_instance.get_list('airplane','plane_licences') 
  # new_list = new_instance.get_list('worktrip', 'workschedule', '2019-12-20', '14')
  # new_list  = new_instance.get_list("worktrip", "available_employees", "2019-12-20", role='Pilot', rank='', a_license='Fokker232')
  print(new_list)


  # new_list = new_instance.get_list('employee')
  #new_list = new_instance.get_list('airplane')
  # new_list = new_instance.get_list('destination')
  # new_list = new_instance.get_list('worktrip')
  #new_list = new_instance.get_list('worktrip',"available_employees",'2019-12-19', '1')
  #new_list = new_instance.get_list(keyword='worktrip', list_type= 'workschedule', searchparam='2019-12-11', _id='14')
  #new_list = new_instance.get_list('airplane','plane_licences')
  #print(new_list)
  
  #print('not working ', new_list)

  # new_instance = EmployeeLL()
  # new_list = new_instance.working_employees([['Köben','1','2','3','4','5'],['Stockholm','6','7','8','9','10']])
  # print(new_list)


  return

  
if __name__ == "__main__":
    main()
