#All calls UI needs to use - forwards calls to the right Class in LL
#10 stafa númer
def check_ssn(ssn):
    if ssn == "" or len(ssn) != 10:
        return False
    
    try: 
        int(ssn)
    except:
        return False
    return True

#Strengur og númer
def check_address(address):
    if address == "":
        return False
    #   return "Heimilisfang vantar"

#strengur@strengur.strengur
def check_email(email):
    if email == "":
        return False

#7 stafa tala XXXXXXX
def check_cellphone(cellphone):
    if cellphone == "":
        return False
    if len(cellphone) > 7:
        return False


def main():
    c = 3333453
    a = check_cellphone(c)
    

    return

#if __name__ == "__main__":
    #main()