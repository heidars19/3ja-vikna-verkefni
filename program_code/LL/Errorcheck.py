from textwrap import wrap
import datetime
from datetime import timedelta
from LL.LL_API import LL_API


class ErrorCheck:
    
    
    ERROR_KENNITALA = 'Ólögleg kennitala!'
    ERROR_EMAIL = 'Ólöglegt netfang'
    ERROR_ADDRESS = 'Ólögleg heimilisfang'
    ERROR_CELLPHONE = "Ólögleg símanúmer"
    ERROR_CLOCK = "Ólöglegur tími"
    ERROR_NAME = "Ólöglegt nafn"
    
    def __init__(self, e_mail=None, ssn=None, address=None, cellphone=None, clock=None, name=None):
        self.__email = e_mail
        self.__ssn = ssn
        self.__address = address
        self.__cellphone = cellphone
        self.__clock = clock
        self.__name = name
            
    def set_mail(self, e_mail) :
        self.__email = e_mail
        
    def set_ssn(self, ssn) :   
        self.__ssn = ssn
        
    def set_address(self, address) :    
        self.__address = address
        
    def set_cellphone(self, cellphone) :    
        self.__cellphone = cellphone
    
    def set_clock(self,clock):
        self.__clock = clock

    def set_name(self,name):
        self.__name = name


    def check_ssn(self):
        '''
        Checks if ssn (kennitala) is valid, returns True or an error string.
        '''
        now = datetime.datetime.now()
        if not self.__ssn.isdigit() :
            return self.ERROR_KENNITALA
        
        if len(self.__ssn) == 10:
            try:
                ssn_list = wrap (self.__ssn, 2)
                ssn_list = [int(n) for n in ssn_list]
                if ssn_list[0] < 1 or ssn_list[0] > 31:
                    return self.ERROR_KENNITALA
                if ssn_list[1] < 1 or ssn_list[1] > 12:
                    return self.ERROR_KENNITALA
                if ssn_list[4]%10==0:
                    birthyear = ssn_list[2]+2000
                if ssn_list[4]%10==9:
                    birthyear = ssn_list[2]+1900
                if birthyear > now.year:
                    return "Back to the future?"
                if birthyear < 1903:
                    return "When i was young in 1900...."
                if  ssn_list[4]%10 != 0 and ssn_list[4]%10 != 9:
                    return self.ERROR_KENNITALA
                return True
            except:
                return self.ERROR_KENNITALA
        else:
            return self.ERROR_KENNITALA


    def check_address(self):
        '''
        Checks if address is valid, returns True or an error string.
        '''
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.éýúíóðáæþöÉÝÚÍÓÐÁÆÞÖ ")
        for character in self.__address:
            if character not in allowed_chars:
                return self.ERROR_ADDRESS
            
        if len(self.__address) < 2 :
            return self.ERROR_ADDRESS
        return True 


    def check_mail(self):
        '''
        Checks if e-mail is valid, returns True or an error string.
        '''
        email_list = self.__email.split ('@')
        if len(email_list) != 2 :
            return self.ERROR_EMAIL
        
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.")
        for character in email_list[1] :
            if character not in allowed_chars:
                return self.ERROR_EMAIL
            
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.!#$%&'*+/=?^_`{|}~")
        for character in email_list[0] :
            if character not in allowed_chars:
                return self.ERROR_EMAIL
            
        email_list[1] = email_list[1].split('.')
        if len(email_list[1]) >= 2 and len(email_list[1][1]) > 1:
            return True
        else:
            return self.ERROR_EMAIL
        
        
    def check_cellphone(self):
        '''
        Checks if phone number is valid, returns True or an error string.
        '''
        if len(self.__cellphone) < 7:
            return self.ERROR_CELLPHONE
        
        if not self.__cellphone.isdigit():
            return self.ERROR_CELLPHONE
        
        return True
    
    def check_clock(self):
        try:
            hours = int(self.__clock[0:2])
            _dot = self.__clock[2:3]
            minutes = int(self.__clock[3:5])
            if hours > 23 or hours < 0:
                return self.ERROR_CLOCK
            if _dot != ":":
                return self.ERROR_CLOCK
            if minutes > 59 or minutes < 0:
                return self.ERROR_CLOCK
            return True
        except:
            return self.ERROR_CLOCK
        
    def check_name(self):
        if len(self.__name) < 3:
            return self.ERROR_NAME
        for i in self.__name:
            if i.isdigit():
                return self.ERROR_NAME
        return True
    
    
    def check_worktrip_date(self, date) :
        '''
        Checks date of departure\n
        date='YYYY-MM-DD HH:MM"
        '''
        worktrips = LL_API()
        worktrip_list = worktrips.get_list('worktrip')
        worktrip_list.pop(0)

        start_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M') - datetime.timedelta(minutes=10)
        end_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M') + datetime.timedelta(minutes=10)

        for line in worktrip_list:
            if len(line[5]) < 17 :
                line[5] += ':00'

            if datetime.datetime.strptime(line[5], '%Y-%m-%d %H:%M:%S') > start_date and datetime.datetime.strptime(line[5], '%Y-%m-%d %H:%M:%S') < end_date :
                return False # Found a worktrip within allowed time
        return True
    
    
def main():
    
    check = ErrorCheck()    
    
    check.set_ssn("2001765459")
    result = check.check_ssn()
    # print(f"Kennitala: {result}")  
         
    check.set_mail("heidars19@ru.is")
    result = check.check_mail()
    # print(f"E-mail: {result}")    

    check.set_address("Hænsnagarður 6")
    result = check.check_address()
    # print(f"Address: {result}")  
       
  
    check.set_cellphone("2001765459")
    result = check.check_cellphone()
    # print(f"Sími: {result}") 

    check.set_clock("24:59")
    result = check.check_clock()
    print(f"Clock: {result}")

    check.set_name("Ófeigur Atli")
    result = check.check_name()
    print(f"name: {result}")
    
    # check = check_ssn("2001765449")
    # print(f"Kennitala: {check}")    
    # check = check_address("Hænsnagarður 6")
    # print(f"Address: {check}")    
    # check = check_cellphone("8221448")
    # print(f"Cellphone: {check}")

    return
    

if __name__ == "__main__":
    main()
