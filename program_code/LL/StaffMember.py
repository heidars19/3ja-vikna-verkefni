class StaffMember:

    def __init__(self,ssn,name,address,mobile,email): 

        self.ssn = ssn
        self.name = name
        self.address = address
        self.mobile = mobile
        self.email = email

    def append_data_to_file(self): 
        pass
    def read_line_in_file(self, data):
        pass
    def change_line(self,line,filename,):
        pass
    
staff1 = StaffMember('2990012394','Eyþór','þingás','eythorb19@marel.com','mail')
print(staff1.name)
print(help(StaffMember))