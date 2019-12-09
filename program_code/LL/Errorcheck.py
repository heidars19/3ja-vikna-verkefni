from textwrap import wrap
import datetime

ERROR_KENNITALA = 'Kennitala ranglega slegin inn!'
ERROR_EMAIL = 'Netfang ranglega slegið inn!'
ERROR_ADDRESS = 'Heimilisfang ranglega slegið inn'
ERROR_CELLPHONE = "Símanúmer ranglega slegið inn!"



def check_ssn(ssn):
    '''
    Checks if ssn (kennitala) is valid, returns True or an error string.
    '''
    now = datetime.datetime.now()
    if not ssn.isdigit() :
        return ERROR_KENNITALA
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


def check_address(address):
    '''
    Checks if address is valid, returns True or an error string.
    '''
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.éýúíóðáæþÉÝÚÍÓÐÁÆÞ ")
    for character in address:
        if character not in allowed_chars:
            return ERROR_ADDRESS
    if len(address) < 2 :
        return ERROR_ADDRESS
    return True 


def check_mail(email):
    '''
    Checks if e-mail is valid, returns True or an error string.
    '''
    email_list = email.split ('@')
    if len(email_list) != 2 :
        return ERROR_EMAIL
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.")
    for character in email_list[1] :
        if character not in allowed_chars:
            return ERROR_EMAIL
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.!#$%&'*+/=?^_`{|}~")
    for character in email_list[0] :
        if character not in allowed_chars:
            return ERROR_EMAIL
    email_list[1] = email_list[1].split('.')
    if len(email_list[1]) >= 2 and len(email_list[1][1]) > 1:
        return True
    else:
        return ERROR_EMAIL
    
    
def check_cellphone(cellphone):
    '''
    Checks if phone number is valid, returns True or an error string.
    '''
    if len(cellphone) < 7:
        return ERROR_CELLPHONE
    if not cellphone.isdigit():
        return ERROR_CELLPHONE
    return True



def main():
    check = check_mail("heidar@fss.is")
    print(f"E-mail: {check}")    
    check = check_ssn("2001765449")
    print(f"Kennitala: {check}")    
    check = check_address("Hænsnagarður 6")
    print(f"Address: {check}")    
    check = check_cellphone("8221448")
    print(f"Cellphone: {check}")

    return
    

if __name__ == "__main__":
    main()
