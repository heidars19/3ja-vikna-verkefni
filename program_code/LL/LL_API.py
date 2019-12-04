#All calls UI needs to use - forwards calls to the right Class in LL
#10 stafa númer
from Employee import Employee
import EmployeeLL

def create_employee(ssn,name,address,mobile,email,role,rank,licence):
    
    Newemp = Employee(ssn,name,address,mobile,email,role,rank,licence)
    return Newemp
   # EmployeeLL.Write(Newemp)


   # Newemp = Employee.from_string(new_emp)

    

#if __name__ == "__main__":


    #main()



#new_emp = '2501952149,Eyþór Óli Borgþórsson,Þingás 31,8453474,eythoroli95@gmail.com,Pilot,Copilot,Fokker232'
emp = create_employee("2501952149","Eyþór Óli Borgþórsson","Þingás 31","8453474","eythoroli95@gmail.com","Pilot","Copilot","Fokker232")

print(emp)
