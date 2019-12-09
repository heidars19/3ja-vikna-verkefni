from textwrap import wrap
import datetime
import string

ERROR_KENNITALA = 'Kennitala ekki lögleg!'
ERROR_EMAIL = 'Invalid e-mail address!'
ERROR_ADDRESS = 'Vinsamlega skráið heimilisfang starfsmanns!'
ERROR_CELLPHONE = "Lengd símanúmers er að lámarki 7 stafir!"


#10 stafa númer
def check_ssn(ssn):
    now = datetime.datetime.now()
    
    if len(ssn) == 10:
        try:
            ssn_list = wrap (ssn, 2)
            ssn_list = [int(n) for n in ssn_list]
            if ssn_list[0] < 1 or ssn_list[0] > 31:
                return ERROR_KENNITALA
            if ssn_list[1] < 1 or ssn_list[1] > 12:
                return ERROR_KENNITALA
            if ssn_list[4]%10==0:
                birthyear = ssn_list[2]+2000
            if ssn_list[4]%10==9:
                birthyear = ssn_list[2]+1900
            if birthyear > now.year  or birthyear < 1903:
                return ERROR_KENNITALA
            if  ssn_list[4]%10 != 0 and ssn_list[4]%10 != 9:
                return ERROR_KENNITALA
            return True
        except:
            return ERROR_KENNITALA
    else:
        return ERROR_KENNITALA

#Strengur og númer
def check_address(address):
    if address == "":
        return ERROR_ADDRESS


#strengur@strengur.strengur
def check_mail(email):
    email_list = email.split ('@')
    if len(email_list) != 2 :
        return ERROR_EMAIL
    for character in email_list[0] :
        if character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'*+-/=?^_`{|}~."
            return ERROR_EMAIL
    for character in email_list[1] :
        if character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-."
            return ERROR_EMAIL
    
    email_list[1] = email_list[1].split('.')

    if len(email_list[1]) >= 2 and len(email_list[1][1]) > 1:
        return True
    else:
        return ERROR_EMAIL
    
#7 stafa tala XXXXXXX
def check_cellphone(cellphone):
    if len(cellphone) > 7:
        return True
    else:
        return ERROR_CELLPHONE



def main():
    check = check_mail("heidar@fss.is")
    print(check)
    
    
    
    
    pass
    

if __name__ == "__main__":
    main()



