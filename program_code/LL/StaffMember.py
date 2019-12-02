class StaffMember:

    def __init__(self,socialsecurity,name,address,email,homephone,cellphone): 

        self.socialsecurity = socialsecurity
        self.name = name
        self.address = address
        self.email = email
        self.homephone = homephone
        self.cellphone = cellphone



    #    if staff_list[0] = "":
            #senda upplýsingar til baka til UI, vantar að fylla inn kennitölu
       # if staff_list[1] = "":
            #senda til baka, vantar að fylla inn nafn

#skilyrði - senda til baka allt sem er il legal


    def append_data_to_file(self,datalist,socialsecurity,header):
        pass
    def read_line_in_file(self, data):
        pass
    def change_line(self,line,filename,):
        pass
    
staff1 = StaffMember('2990012394','Eyþór','þingás','eythorb19@marel.com','5594489','93434242')
print(staff1.name)