


AIRPLANE = ("   __|__   ","--@-(_)-@--"," !  !  !  ")
AIRPORT = '\n\
  _\n\
 | |\                                                         ===================\n\
===| \______________|_______                                  |  NaNTMAirTMHQ   |\n\
  \|  O ooooo-=====-|ooo O n\__                               |      _____      |\n\
    -|=|--o-----||--|---|=||---’  _o’     o   .        o o    | $$  |  |  |  $$ |\n\
_____|=|__|\___oo______|=|o________|_____|\   |     ___|\|\__ |_____|  |  |_____|'

AIRPORT2 = '\n\
                                            __|__\n\
  _                                     ---@-(")-@---\n\
 | |\                                      !  !  !            ===================\n\
===| \______________|_______                                  |  NaNTMAirTMHQ   |\n\
  \|  O ooooo-=====-|ooo O n\__            . . . .            |      _____      |\n\
    -|=|--o-----||--|---|=||---’  _o’     o   .        o o    | $$  |  |  |  $$ |\n\
_____|=|__|\___oo______|=|o________|_____|\   |     ___|\|\__ |_____|  |  |_____|'

print("\033[0;37;40m") # Sets font to white (37) and background to black (40)

def menu_box (option, menu_object, length) :
    buffer_list = []
    menu_string = str(option) + " " + menu_object
    menu_string = "|" + "{:<{:}}".format(menu_string, length) + "|"
    buffer_list.append(menu_string)
    return menu_string


def make_user_interface(interface_list):
    
    header_string = "+-----------------------+"
    userface_list = []
    interface_string = ""
    for i in range(len(interface_list)):
        buffer_list = []
    
        for x in range(len(interface_list[i])):
            buffer_list.append(menu_box(x+1, interface_list[i][x], len(header_string)-2))
        userface_list.append(buffer_list)
    for i in range(len(AIRPLANE)):
        interface_string += "{:>{lengd:}}".format(AIRPLANE[i],lengd = (len(header_string)-2) * len(userface_list) ) + "\n"
    for i in range(len(userface_list)):
        interface_string += header_string + " "
    interface_string += "\n"
    for i in range(len(userface_list)):
        for x in range(len(userface_list[i])):
            for y in range(len(userface_list)):
                interface_string += userface_list[i+y][x] + " "
            interface_string += "\n"
        for i in range(len(userface_list)):
            interface_string += header_string + " "
        interface_string += AIRPORT
        return interface_string
    
    

def select_menu():
    while True:
        selected_menu = input("Select option: ")
        if selected_menu == "1":
            return True
        elif selected_menu == "2":
            return True
        elif selected_menu == "3":
            return True
        elif selected_menu == "4":
            return False
        else:
            print("Wrong selection")


MENU1 = ("\033[0;31;40mDeildarstjóri \033[0;37;40m ", "Vaktstjóri", "Quit")
MENU2 = ("Max","*Boeing*","Back")
MENU3 = ("*Nuuk*","Þórshöfn","Back")
def main():
    interface_list = (MENU1, ) # Skilja eftir kommu til að fá ekki villu ;)
    interface_string = make_user_interface(interface_list)
    print(interface_string)
    """
    if select_menu():
        interface_list = ("WoopWoop", "We DID IT")
        interface_string = make_user_interface(interface_list)
        print(interface_string)
        """
    #print("\033[1;32;40m Bright Green  \n")

main()
