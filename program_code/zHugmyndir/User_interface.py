import sys
import os
def make_user_interface(interface_list):
    print("          __|__\n\
       --@-(_)-@--\n\
         !  !  !")
    header_string = "+-----------------------+"
    interface_string = header_string
    
    for i in range(len(interface_list)):
        buffer_string = str(i+1) + " " + interface_list[i]
        interface_string += "\n" + "|" + "{:^{lengd:}}".format(buffer_string, lengd = len(header_string)-2) + "|"
    interface_string += "\n" + header_string
    interface_string += '\n                                            __|__\n_                                       ---@-(")-@---\n| |\                                       !  !  !            ===================\n===| \______________|_______                                  |  NaNTMAirTMHQ   |\n  \|  O ooooo-=====-|ooo O n\__            . . . .            |      _____      |\n    -|=|--o-----||--|---|=||---’  _o’     o   .        o o    | $$  |  |  |  $$ |\n_____|=|__|\___oo______|=|o________|_____|\   |     ___|\|\__ |_____|  |  |_____|'
    return interface_string

def make_user_interface_1(interface_list):
    airplane = ("   __|__   ","--@-(_)-@--"," !  !  !  ")
    header_string = "+-----------------------+"
    userface_list = []
    interface_string = ""
    for i in range(len(interface_list)):
        buffer_list = []
    
        for x in range(len(interface_list[i])):
            buffer_string = str(x+1) + " " + interface_list[i][x]
            buffer_string2 = "|" + "{:^{lengd:}}".format(buffer_string, lengd = len(header_string)-2) + "|"
            buffer_list.append(buffer_string2)
        userface_list.append(buffer_list)
    airport = '\n_\n| |\                                                          ===================\n===| \______________|_______                                  |  NaNTMAirTMHQ   |\n  \|  O ooooo-=====-|ooo O n\__                               |      _____      |\n    -|=|--o-----||--|---|=||---’  _o’     o   .        o o    | $$  |  |  |  $$ |\n_____|=|__|\___oo______|=|o________|_____|\   |     ___|\|\__ |_____|  |  |_____|'
    for i in range(len(airplane)):
        interface_string += "{:>{lengd:}}".format(airplane[i],lengd = (len(header_string)-2) * len(userface_list) ) + "\n"
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
        interface_string += airport
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


def main():
    interface_list = (("*Deildarstjóri*", "Vaktstjóri", "Quit"),("Max","*Boeing*","Back",),("*Nuuk*","Þórshöfn","Back"))
    interface_string = make_user_interface_1(interface_list)
    print(interface_string)
    """
    if select_menu():
        interface_list = ("WoopWoop", "We DID IT")
        interface_string = make_user_interface(interface_list)
        print(interface_string)
        """


main()
