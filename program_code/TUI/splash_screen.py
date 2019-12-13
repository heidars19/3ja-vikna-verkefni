import time
import sys
"""import curses
import blessed"""
empty_space = "\n"*20
airplane = \
("   __|__   "\
,"--@-(_)-@--"\
,"  !  !  !  ")
breyta = "hallo        "
airport = \
'\n_\n\
| |\                                                          ===================\n\
===| \______________|_______                                  |    NaN Air HQ   |\n\
  \|  O ooooo-=====-|ooo O n\__                               |      _____      |\n\
    -|=|--o-----||--|---|=||---’  _o’     o   .        o o    | $$  |  |  |  $$ |\n\
_____|=|__|\____oo______|=|o________|_____|\   |    ___|\|\__ |_____|  |  |_____|'
flying_plane = \
("           _       "\
,"         -=\`\     "\
,"     |\ ____\_\__  "\
,'   -=\c`""""""" "`)'\
,"      `~~~~~/ /~~` "\
,"        -==/ /     "\
,"          '-'      ")
header_string = "+-----------------------+"
empty_string = "                         "

logo = [\
"               ███╗   ██╗ █████╗ ███╗   ██╗     █████╗ ██╗██████╗\n",
"               ████╗  ██║██╔══██╗████╗  ██║    ██╔══██╗██║██╔══██╗\n",
"               ██╔██╗ ██║███████║██╔██╗ ██║    ███████║██║██████╔╝\n",
"               ██║╚██╗██║██╔══██║██║╚██╗██║    ██╔══██║██║██╔══██╗\n",
"               ██║ ╚████║██║  ██║██║ ╚████║    ██║  ██║██║██║  ██║\n",
"               ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝\n",
"                     ~ Where Dividing by Zero Makes Sense ~      \n",]

def make_user_interface_1(interface_list):
    userface_list = []
    interface_string = ""
    userface_list = make_complex_userfacelist(interface_list)
    interface_string = make_static_plane(interface_string,userface_list)
    interface_string = make_logo(interface_string)
    interface_string += airport
    return interface_string

def make_user_interface_fly(interface_list, len_fly = 0):
    userface_list = []
    interface_string = ""
    userface_list = make_complex_userfacelist(interface_list)
    interface_string = make_flying_plane(interface_string, userface_list, len_fly)
    interface_string = make_logo(interface_string)
    interface_string += airport
    return interface_string

def get_longest_sublist(list_to_check):
    longest = 0
    list_len = 0
    for i in range(len(list_to_check)):
        if len(list_to_check[i]) > longest:
            longest = len(list_to_check[i])
            list_index = i
        else:
            list_len
    return longest, list_index

def make_complex_userfacelist(interface_list):
    userface_list =[]
    for_len, list_index = get_longest_sublist(interface_list)
    stop = []
    go = 0
    for i in range(len(interface_list)):
            buffer_list = []
            for x in range(for_len+1):
                try:
                    if x != for_len:
                        buffer_string = str(x+1) + " " + interface_list[i][x]
                        buffer_string2 = "|" + "  {:<{lengd:}}".format(buffer_string, lengd = len(header_string)-4) + "|"
                        buffer_list.append(buffer_string2)
                    else:
                        if list_index == i:
                            buffer_string2 = header_string
                            buffer_list.append(buffer_string2)
                        else:
                            buffer_string2 = empty_string
                            buffer_list.append(buffer_string2)
                except:
                    if i not in stop:
                        buffer_string2 = header_string
                        buffer_list.append(buffer_string2)
                        stop.append(i)
                        go = 1
                    else:
                        buffer_string2 = empty_string
                        buffer_list.append(buffer_string2)
                    
                
            userface_list.append(buffer_list)
    return userface_list

def add_header(interface_string, userface_list):
    for i in range(len(userface_list)):
        interface_string += header_string + " "
    interface_string += "\n"
    return interface_string

def add_footer(interface_string, userface_list):
    for i in range(len(userface_list)):
        interface_string += header_string + " "
    interface_string += "\n"
    return interface_string
def make_box_multi(interface_string, userface_list):
    
    for i in range(len(userface_list)):
        for x in range(len(userface_list[i])):
            for y in range(len(userface_list)):
                try:
                    interface_string += userface_list[i+y][x] + " "
                except:
                    continue
            interface_string += "\n"
        return interface_string

def make_box_simple(userface_list, interface_string):
    for i in range(len(userface_list)):
        interface_string += userface_list[i] + " "
        interface_string += "\n"
    return interface_string

def make_flying_plane(interface_string, userface_list, len_fly = 0):
    for i in range(len(flying_plane)):
        interface_string += "{:>{lengd:}}".format(flying_plane[i],lengd = ((len(header_string)+2) * (len(userface_list)+1))-len_fly-5) + "\n"
    return interface_string

def make_static_plane(interface_string,userface_list):
    for i in range(len(airplane)):
            interface_string += "{:>{lengd:}}".format(airplane[i],lengd = ((len(header_string)) * len(userface_list))+len(userface_list)+9) + "\n"
    return interface_string



def main2():
    interface_list = [("*Deildarstjóri*","blah", "Vaktstjóri", "Quit"),("Max","*Boeing*","blah","blah","blah","Back",),("*Nuuk*","blah","blah","Þórshöfn","Back")]
    interface_list2 = [("*Deildarstjóri*","blah", "Vaktstjóri", "Quit"),("Max","*Boeing*","blah","blah","blah","Back",)]
    interface_list3 = [("*Deildarstjóri*","blah", "Vaktstjóri", "Quit")]
    print(empty_space)
    interface_string = make_user_interface_1(interface_list3)
    print(interface_string)
    for i in range(21):
        print(empty_space)
        print(empty_space)
        interface_string = make_user_interface_fly(interface_list3,10-i)
        print(interface_string)
        time.sleep(.04)
    print(empty_space)
    interface_string = make_user_interface_1(interface_list2)
    print(interface_string)

def make_logo(interface_string):
    for i in range(len(logo)):
        interface_string += logo[i]
    return interface_string

main2()