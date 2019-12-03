class Employee:

    def __init__(self,ssn,name,address,mobile,email,role,rank,licence): 

        self.__ssn = ssn
        self.__name = name
        self.__address = address
        self.__mobile = mobile
        self.__email = email
        self.__role = role
        self.__rank = rank
        self.__licence = licence


    def __str__(self):
        return f' {self.__ssn},{self.__name},{self.__address},{self.mobile},{self.email},{self.role},{self.rank},{self.licence}

    def set(self, infotype, new_info):
        self.personalinfo[infotype] = new_info

        name, "Guðný"
        self.name = "Guðný"
    


staff1 = Employee('2501952149','Eyþór Óli','Þingás 31','8453474','eythorb19@marel.com','Meistari','Pilot','Fokker 484')
set()

print(staff1)
x = str(staff1)
print(x)

#print(staff1.__name)
#print(help(Employee))
# 

class Student(object):
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    def setGrade(self, course, grade):
        self.grades[course] = grade

    def getGrade(self, course):
        return self.grades[course]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)
    def __str__(self):
        if self.gender == "male":
            return str(self.name) + " is a " + str(self.age) + " years old " + str(self.gender) + " his grades are: " + str(self.grades)
        elif self.gender == "female":
            return str(self.name) + " is a " + str(self.age) + " years old " + str(self.gender) + " her grades are: " + str(self.grades)

# Define some students
john = Student("John", 12, "male", 6, {"math":3.5, "computer":3})
jane = Student("Jane", 12, "female", 6, {"math":3.5})

# Now we can get to the grades easily
jane.setGrade("computer", 3)
print(john.getGrade("computer"))
print(john.getGPA())
print(jane.getGPA())
print(john)
print(jane)