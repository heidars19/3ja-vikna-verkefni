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
                return False, 'Kennitala ekki lögleg.'
            if ssn_list[1] < 1 or ssn_list[1] > 12:
                return False, 'Kennitala ekki lögleg.'
            if ssn_list[4]%10==0:
                birthyear = ssn_list[2]+2000
            if ssn_list[4]%10==9:
                birthyear = ssn_list[2]+1900
            if birthyear > now.year  or birthyear < 1903:
                return False, 'Kennitala ekki lögleg.'
            if  ssn_list[4]%10 != 0 and ssn_list[4]%10 != 9:
                return False, 'Kennitala ekki lögleg.'
            return True
        except:
            return False, ('Kennitala ekki lögleg')
    else:
        return False, ('Kennitala ekki lögleg.') 

#Strengur og númer
def check_address(address):
    if address == "":
        return False, 'Vinsamlega skráið heimilisfang starfsmanns'


#strengur@strengur.strengur
def check_mail(email):
    email_list = email.split ('@')
    email_list[1] = email_list[1].split('.')
    print ()
    if len(email_list)==2 and len(email_list[1])==2 and len(email_list[1][1]) > 1:
        return True
    else:
        return False, 'Invalid e-mail address!'
    
#7 stafa tala XXXXXXX
def check_cellphone(cellphone):
    if len(cellphone) > 7:
        return True
    else:
        return False, ("Lengd símanúmers er að lámarki 7 stafir")



def main():
    

if __name__ == "__main__":
    main()



