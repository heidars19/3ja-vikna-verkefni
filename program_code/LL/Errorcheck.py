from textwrap import wrap
import datetime
#10 stafa númer
def check_ssn(ssn):
    now = datetime.datetime.now()
    
    if len(ssn) == 10:
        try:
            ssn_list = wrap (ssn, 2)
            ssn_list = [int(n) for n in ssn_list]
            if ssn_list[0] < 1 or ssn_list[0] > 31:
                return True, ('Kennitala ekki lögleg.')
            if ssn_list[1] < 1 or ssn_list[1] > 12:
                return True, ('Kennitala ekki lögleg.')
            if ssn_list[4]%10==0:
                birthyear = ssn_list[2]+2000
            if ssn_list[4]%10==9:
                birthyear = ssn_list[2]+1900
            if birthyear > now.year  or birthyear < 1903:
                return True, ('Kennitala ekki lögleg.')
            if  ssn_list[4]%10 != 0 and ssn_list[4]%10 != 9:
                return True, ('Kennitala ekki lögleg.')
            return 'kennitala logleg'
        except:
            return True, ('Kennitala ekki lögleg')
    else:
        return True, ('Kennitala ekki lögleg.') 

#Strengur og númer
def check_address(address):
    if address == "":
        return True, 'Vinsamlega skráið heimilisfang starfsmanns'


#strengur@strengur.strengur
def check_mail(email):
    email_list = email.split ('@')
    email_list[1] = email_list[1].split('.')
    print ()
    if len(email_list)==2 and len(email_list[1])==2 and len(email_list[1][1]) > 1:
        return False
    else:
        return True, 'Invalid e-mail address!'
    
#7 stafa tala XXXXXXX
def check_cellphone(cellphone):
    if len(cellphone) > 7:
        return False
    else:
        return True, ("Lengd símanúmers er að lámarki 7 stafir")



def main():
    print(check_ssn('0810015920'))    

if __name__ == "__main__":
    main()



