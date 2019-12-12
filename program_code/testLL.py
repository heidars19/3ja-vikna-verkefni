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
  #return_value = new_instance.create("worktrip",('','','','Reykjavik','Manchester','2019-12-20 06:45:00','5','1','2','3','4','5','Staffed','')) # dest_id, departure_time, airplane_id
  #return_msg(return_value, f"creating a new object, code:{return_value}")
#return_value = new_instance.create("worktrip",('1','2019-12-19 11:45','5'))



  #CHANGE
  # return_value = new_instance.change("destination",('16','Milano', 'Italy','6:30:10','2.100','John Philips','0219933884','BC_airport','2019-12-08 13:41:20.362544'))
  # return_value = new_instance.change("employee",('23','2001933874', 'Gömul Lára','Bústaðarvegi 6','8922773','gamla@geit.org','Pilot','Captain','F1Fighters','2019-12-08 12:46:12.455312'))
  # return_value = new_instance.change("airplane",('73','TF-breytt', 'NAbreytt','Fokker','F800','Breytt','13:25:38.975230'))
  # return_value = new_instance.change("worktrip",('13','Milano', 'Italy','6:30:10','2.100','John Philips','0219933884','BC_airport','2019-12-07 21:39:33.300255'))
  # return_msg(return_value, f"changing, code:{return_value}")
  #return_value = new_instance.change("worktrip",('14','NA2275','NA3525','Keflavik','súðavík','2019-12-30 06:21:00','2019-12-19 22:00:00','3','13','12','13','14','15','Mönnuð','2019-12-05 20:45:18.095017'))

  
  #GET_LIST
  
  #new_list = new_instance.get_list('employee')
  #new_list = new_instance.get_list('airplane')
  # new_list = new_instance.get_list('destination')
  # new_list = new_instance.get_list('worktrip')
  # new_list = new_instance.get_list('worktrip',"working_employees",'2019-12-20')
  # new_list = new_instance.get_list('destination',"destination_id","Vancouver")
  # new_list = new_instance.get_list('airplane','plane_licences') 
  #new_list = new_instance.get_list('worktrip', 'work_schedule', '2019-12-25', '23')
  
  #Work Schedule test:  
  # new_list = new_instance.get_list('worktrip', 'work_schedule', '2019-12-01', '', days=1) #fær öll flug fyrir einn dag ákveðna dagsetningu
  # new_list = new_instance.get_list('worktrip', 'work_schedule', '2019-12-01') #fær flug fyrir öll flug áveðna viku
  # new_list = new_instance.get_list('worktrip', 'work_schedule', '2019-12-01', '1') #fær flug fyrir ákveðinn starfsmann ákveðna viku

  #Worktrip translator:
  new_list = new_instance.get_list(list_type='worktrip_readable', searchparam=(15,'NA156','NA157','Keflavík','15','2019-12-20 11:50:00','2019-12-20 21:45:00','5','3','2','7','11','15','18','2019-12-11 01:51:02.065347'))


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


  return None

  
if __name__ == "__main__":
    main()