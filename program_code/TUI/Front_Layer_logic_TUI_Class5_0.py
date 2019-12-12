#import User_interface
"""from LL.LL_API_sigurgeir import *
from LL.LL_API_eythor import *
from LL.LL_API_offi import *"""
from LL.LL_API import *
import os
#import Front_layer_TUI
import locale
import curses
import time
import datetime
#import dateutil.parser
import calendar
from LL.Errorcheck import *

#from LL.LL_API_eythor import *
from curses import wrapper, color_pair
from curses.textpad import Textbox, rectangle
header_lengd = 20
os.system('mode con: cols=150 lines=30')  # works on M$ Windows
# coding = UTF-8

class TUI():
    def __init__(self,stdscr):
        self.menu_select = 0
        self.exeption = 0
        self.exeption2 = 0
        self.new_registration = False
        self.stdscr = stdscr
        self.new_reg_u_input = False
        self.highlight_main_list = ["x", " ", " "]
        self.list_line_index = 0
        self.check_specifcly = False
        self.instance_API = LL_API()
        self.next_section = 0
        self.item_list = self.instance_API.get_list("employee")
        self.header_len = []
        self.index_len = []
        self.errorcheck = ErrorCheck()
    def construct_TUI(self,x_list):
        main_menu_temp = self.construct_main_menu()
        if self.new_registration == True:
            body_temp = self.construct_body_new_registration()
        elif self.check_specifcly == True:
            body_temp = self.construct_body_new_registration()
        else:    
            body_temp = self.construct_body_lists()
        header_temp = self.construct_header()
        footer_temp = self.construct_footer(x_list)
        self.TUI_list = []
        self.create_TUI_list(main_menu_temp)
        self.create_TUI_list(header_temp)
        self.create_TUI_list(body_temp)
        self.create_TUI_list(footer_temp)
        return self.TUI_list

    def create_TUI_list(self,any_list):
        for i in range(len(any_list)):
            self.TUI_list.append(any_list[i])

    def construct_main_menu(self):
        menu = ("1.Starfsmenn", "2.Vinnuferðir", "3.Áfangastaðir", "4.Flugvélar")
        self.date = datetime.date.today().strftime("%d %b %Y")
        get_date = "{:^{lengd:}}".format(self.date,lengd = header_lengd)
        main_menu_length = 20
        m_starf = "{:^{lengd:}}".format(menu[0],lengd = main_menu_length)
        m_vinnufe = "{:^{lengd:}}".format(menu[1],lengd = main_menu_length)
        m_afangas = "{:^{lengd:}}".format(menu[2],lengd = main_menu_length)
        m_flugvel = "{:^{lengd:}}".format(menu[3],lengd = main_menu_length)
        main_menu_template = (
        (("╔════════════════════╦════════════════════╦════════════════════╦════════════════════╦════════════════════╗")),
        (("║"),(m_starf) ,    ("║") ,(m_vinnufe) , ("║") ,(m_afangas) , ("║"), (m_flugvel) , ("║"),(get_date),    ("║")),
        (("╠════════════════════╩════════════════════╩════════════════════╩════════════════════╝                    ║")))
        return main_menu_template

    def construct_header(self):#("Nafn áfangastaðar:","Land:","Fjarlægð frá Íslandi:", "Nafn tengiliðar:","Neyðarsímanúmer:","Flugvöllur:"),
        self._header = (\
        ("Kennitala","Nafn","Heimilisfang","Sími","Email","Starfsheiti","Titill","Leyfi"),\
        ("Flunúmer út","Flugnúmer heim","Brottför","Áfangastaður","Brottfarartími","Komutími","Flugvél","Captain","Copilot","Fsm","Fa1","Fa2","Staða"),\
        ("Áfangastaður","Land","Flugtími","Fjarlægð frá Íslandi","Tengiliður","Sími","FlugVöllur"),\
        ("Plane_id","Plane_type","Framleiðandi","Sætafjöldi","Nafn"))
        header_string = ""
        for i in range(len(self._header[self.menu_select])):
            try:
                if self.menu_select == 0:
                    if i not in [2,4,7]:
                        header_string += "{:<{lengd:}}".format(self._header[self.menu_select][i],lengd = int(100/5))
                elif self.menu_select == 1:
                    if i not in [0,1,7,8,9,10,11]:
                        header_string += "{:<{lengd:}}".format(self._header[self.menu_select][i],lengd = int(100/6)+2)
                elif self.menu_select == 2:
                    if i not in [2,3]:
                        header_string += "{:<{lengd:}}".format(self._header[self.menu_select][i],lengd = int(100/5))
                else:
                    header_string += "{:<{lengd:}}".format(self._header[self.menu_select][i],lengd = int(100/5))
            except :
                continue
        if len(header_string) > 100:
            for i in range(len(header_string)-100):
                        header_string = header_string[:-1]
        for i in range(100-len(header_string)):
            header_string += " "
        header_template = (
        (("║  "),(header_string),("  ║")),
        )
        return header_template

    def construct_body_lists(self):
        new_list = []
        exceptions = ["", "Pilot", "Cabincrew"]
        rank_exception = [["Captain", "Co-Pilot"],["Flight Service Manager","Flight Attendant"]]
        self.index_len = []
        self.header_len = []
        self.select_len = 0
        try:
            for i in range(len(self.item_list[0])):
                longest = 0
                for x in range(0+self.next_section,len(self.item_list)+self.next_section):
                    try:
                        if len(self.item_list[x][i]) > longest:
                            longest = len(self.item_list[x][i])
                    except:
                        continue
                self.index_len.append(longest)
        except:
            pass
        for i in range(0+self.next_section,15+self.next_section):
            try:
                new_string = ""
                if self.menu_select == 0:
                    for x in range(len(self.item_list[i])):
                        if x not in [0,3,5,8,9]:
                            new_string += "{:<{lengd:}}".format(self.item_list[i][x][0:19],lengd = int(100/5))
                            self.header_len.append(self.index_len[x])
                        if x == 3 or x == 5:
                                self.header_len.append(0)
                    new_list.append(new_string)
                elif self.menu_select == 1:
                    for x in range(len(self.item_list[i])):
                        if x not in [0,1,2,8,9,10,11,12,14]:
                            new_string += "{:<{lengd:}}".format(self.item_list[i][x][0:int(100/6)],lengd = int(100/6)+2)
                            self.header_len.append(self.index_len[x])
                        elif x != 0:
                            self.header_len.append(0)
                    new_list.append(new_string)
                elif self.menu_select == 2:
                    for x in range(len(self.item_list[i])):
                        if x not in [0,3,4,8,9]:
                            new_string += "{:<{lengd:}}".format(self.item_list[i][x][0:19],lengd = int(100/5))
                            self.header_len.append(self.index_len[x])
                        if x in [3,4]:
                            self.header_len.append(0)
                    new_list.append(new_string)
                elif self.menu_select == 3:
                    for x in range(len(self.item_list[i])):
                        if x not in [0,6]:
                            new_string += "{:<{lengd:}}".format(self.item_list[i][x][0:19],lengd = int(100/5))
                            self.header_len.append(self.index_len[x])
                    new_list.append(new_string)
                self.select_len += 1
            except:
                for i in range(15-len(new_list)):
                    new_list.append("")
        for i in range(15-len(new_list)):
            new_list.append("{:^{lengd:}}".format("", lengd = 100))
        for i in range(len(new_list)):
            for x in range(100-len(new_list[i])):
                new_list[i] += " "
            for x in range(len(new_list[i])-100):
                new_list[i] = new_list[i][:-1]
        body_template = (
        (("║ ┌────────────────────────────────────────────────────────────────────────────────────────────────────┐ ║")),
        (("║ │"),(new_list[0]),                                                                                 ("│ ║")),
        (("║ │"),(new_list[1]),                                                                                 ("│ ║")),
        (("║ │"),(new_list[2]),                                                                                 ("│ ║")),
        (("║ │"),(new_list[3]),                                                                                 ("│ ║")),
        (("║ │"),(new_list[4]),                                                                                 ("│ ║")),
        (("║ │"),(new_list[5]),                                                                                 ("│ ║")),
        (("║ │"),(new_list[6]),                                                                                 ("│ ║")),
        (("║ │"),(new_list[7]),                                                                                 ("│ ║")),
        (("║ │"),(new_list[8]),                                                                                 ("│ ║")),
        (("║ │"),(new_list[9]),                                                                                 ("│ ║")),
        (("║ │"),(new_list[10]),                                                                                ("│ ║")),
        (("║ │"),(new_list[11]),                                                                                ("│ ║")),
        (("║ │"),(new_list[12]),                                                                                ("│ ║")),
        (("║ │"),(new_list[13]),                                                                                ("│ ║")),
        (("║ │"),(new_list[14]),                                                                                ("│ ║")),
        (("║ └────────────────────────────────────────────────────────────────────────────────────────────────────┘ ║"))
        )
        return body_template

    def construct_body_new_registration(self):
        self.registration_list = (
            ("Kennitala:","Nafn:","Heimilsfang:","Sími:", "Netfang:","Starfstitill:","Starfsstaða:"),
            ("Dagsetning:","Brottfaratími út:","Upphafsstaður:","Áfangastaður:","Flugvél:"),
            ("Nafn áfangastaðar:","Land:","Flugtími:","Fjarlægð frá Íslandi:", "Nafn tengiliðar:","Neyðarsímanúmer:","Flugvöllur:"),
            ("Plane_id:","Plane_type:","Framleiðandi:","Sætafjöldi:","Nafn:"),
            )
        new_list = []
        new_string = ""
        for i in range(len(self.registration_list[self.menu_select])):
            new_string += "{:<{lengd:}}".format(self.registration_list[self.menu_select][i],lengd = 49)
            new_list.append(new_string)
            new_string = ""
        for i in range(8-len(new_list)):
            new_list.append("{:^{lengd:}}".format("", lengd = 49))
        for i in range(len(new_list)):
            for x in range(49-len(new_list[i])):
                new_list[i] += " "
        body_template = (
        (("║ ┌────────────────────────────────────────────────────────────────────────────────────────────────────┐ ║")),
        (("║ │ "),(new_list[0]),(new_list[4]),                                                                 (" │ ║")),
        (("║ │                                                                                                    │ ║")),
        (("║ │                                                                                                    │ ║")),
        (("║ │                                                                                                    │ ║")),
        (("║ │ "),(new_list[1]),(new_list[5]),                                                                 (" │ ║")),
        (("║ │                                                                                                    │ ║")),
        (("║ │                                                                                                    │ ║")),
        (("║ │ "),(new_list[2]),(new_list[6]),                                                                 (" │ ║")),
        (("║ │                                                                                                    │ ║")),
        (("║ │                                                                                                    │ ║")),
        (("║ │                                                                                                    │ ║")),
        (("║ │ "),(new_list[3]),(new_list[7]),                                                                 (" │ ║")),
        (("║ │                                                                                                    │ ║")),
        (("║ │                                                                                                    │ ║")),
        (("║ │                                                                                                    │ ║")),
        (("║ └────────────────────────────────────────────────────────────────────────────────────────────────────┘ ║"))
        )
        self.new_registration = False
        return body_template

    def box_frame(length, vertical='top'):
        '''
        Send in total length
        '''
        line = '─'
        if vertical == 'top' :
            left_corner = '┌'
            right_corner = '┐'
        else :
            left_corner = '└'
            right_corner = '┘'
        return left_corner + line*(length-2) + right_corner


    MENU_BUTTON_1 = '| Skoða |'
    MENU_BUTTON_2 = '| Nýskrá |'
    MENU_BUTTON_3 = '|Dagsetning|'
    MENU_BUTTON_4 = '| Flokka |'
    MENU_BUTTON_5 = '| Vika  |'

    MENU_BOX_1_LENGTH = len(MENU_BUTTON_1)
    MENU_BOX_2_LENGTH = len(MENU_BUTTON_2)
    MENU_BOX_3_LENGTH = len(MENU_BUTTON_3)
    MENU_BOX_4_LENGTH = len(MENU_BUTTON_4)
    MENU_BOX_5_LENGTH = len(MENU_BUTTON_5)

    MENU_OPTION_1 = 'Allir'
    MENU_OPTION_2 = 'Flugmenn'
    MENU_OPTION_3 = 'Flugþjónar'
    MENU_OPTION_LENGTH = 12 


    def construct_footer(self, x_list):
        top_box1 = TUI.box_frame(self.MENU_BOX_1_LENGTH)
        top_box2 = TUI.box_frame(self.MENU_BOX_2_LENGTH)
        top_box3 = TUI.box_frame(self.MENU_BOX_3_LENGTH)
        top_box4 = TUI.box_frame(self.MENU_BOX_4_LENGTH)
        top_box5 = TUI.box_frame(self.MENU_BOX_5_LENGTH)
        bot_box1 = TUI.box_frame(self.MENU_BOX_1_LENGTH,"not top")
        bot_box2 = TUI.box_frame(self.MENU_BOX_2_LENGTH,"not top")
        bot_box3 = TUI.box_frame(self.MENU_BOX_3_LENGTH,"not top")
        bot_box4 = TUI.box_frame(self.MENU_BOX_4_LENGTH,"not top")
        bot_box5 = TUI.box_frame(self.MENU_BOX_5_LENGTH,"not top")
        check_box_left = " ("
        check_box_right = ")"
        check_box_x = x_list
        one_space_string = "  "
        empty_string1 = "     "
        empty_string2 = "         "
        Flokka_listi = [[
        " {:<{lengd:}}".format(self.MENU_OPTION_1, lengd = self.MENU_OPTION_LENGTH),
        " {:<{lengd:}}".format(self.MENU_OPTION_2, lengd = self.MENU_OPTION_LENGTH),
        " {:<{lengd:}}".format(self.MENU_OPTION_3, lengd = self.MENU_OPTION_LENGTH),
        ],
        [
        " {:<{lengd:}}".format("",lengd = self.MENU_OPTION_LENGTH + 3),
        ]
        ]
        footer = (
        (
        (top_box1,top_box2,top_box3,top_box4, check_box_left + check_box_x[0] + check_box_right + Flokka_listi[0][0]),
        (self.MENU_BUTTON_1,self.MENU_BUTTON_2,self.MENU_BUTTON_3,self.MENU_BUTTON_4, check_box_left + check_box_x[1] + check_box_right + Flokka_listi[0][1]
        ),
        (bot_box1,bot_box2,bot_box3,bot_box4,check_box_left + check_box_x[2] + check_box_right + Flokka_listi[0][2])
        ),
        (
        (top_box1,top_box2,top_box3,top_box5, one_space_string + Flokka_listi[1][0]),
        (self.MENU_BUTTON_1,self.MENU_BUTTON_2,self.MENU_BUTTON_3,self.MENU_BUTTON_5,one_space_string + Flokka_listi[1][0]
        ),
        (bot_box1,bot_box2,bot_box3,bot_box5,one_space_string + Flokka_listi[1][0])
        ),
        (
        (top_box1,top_box2,empty_string2,empty_string2, empty_string1 + Flokka_listi[1][0]),
        (self.MENU_BUTTON_1,self.MENU_BUTTON_2,\
        "{:^{lengd:}}".format("",lengd = 9),\
        "{:^{lengd:}}".format("",lengd = 9) ,
        empty_string1 + Flokka_listi[1][0]
        ),
        (bot_box1,bot_box2,empty_string2,empty_string2,empty_string1 + Flokka_listi[1][0])
        ),
        (
        (top_box1,top_box2,top_box3,empty_string2, one_space_string + Flokka_listi[1][0]),
        (self.MENU_BUTTON_1,self.MENU_BUTTON_2,self.MENU_BUTTON_3,\
        "{:^{lengd:}}".format("",lengd = 9) ,
        one_space_string + Flokka_listi[1][0]
        ),
        (bot_box1,bot_box2,bot_box3,empty_string2,one_space_string + Flokka_listi[1][0])
        )
        )
        
        
        footer_template = (
        (("║ "),(footer[self.menu_select][0][0]),(" "),(footer[self.menu_select][0][1]),(" "),(footer[self.menu_select][0][2]),(" "),(footer[self.menu_select][0][3]),(footer[self.menu_select][0][4]),("                                          ║")),
        (("║ "),(footer[self.menu_select][1][0]),(" "),(footer[self.menu_select][1][1]),(" "),(footer[self.menu_select][1][2]),(" "),(footer[self.menu_select][1][3]),(footer[self.menu_select][1][4]),("                                          ║")),
        (("║ "),(footer[self.menu_select][2][0]),(" "),(footer[self.menu_select][2][1]),(" "),(footer[self.menu_select][2][2]),(" "),(footer[self.menu_select][2][3]),(footer[self.menu_select][2][4]),("                                          ║")),
        (("╚════════════════════════════════════════════════════════════════════════════════════════════════════════╝"))
        )
        return footer_template

    def make_drop_down_menu(self,y,x,text_string_1,text_string_2):
        position_y = 0
        editwin = curses.newwin(2,30,y,x)
        editwin.keypad(1)
        while True:
            editwin.refresh()
            self.drop_down(editwin,text_string_1,text_string_2,position_y)
            button_press = editwin.getch()
            if button_press == curses.KEY_UP or button_press == 450:
                if position_y == 0:
                    position_y = 1
                else:
                    position_y -= 1
            elif button_press == curses.KEY_DOWN or button_press == 456:
                if position_y == 1:
                    position_y = 0
                else:
                    position_y += 1
            elif button_press == 10:
                if position_y == 0:
                    return text_string_1
                else:
                    return text_string_2

    def make_plane_license_dropdown(self,y,x,create = 0):
        """This method gets all airplane licenses and creates a drop down menu for the user"""
        position_y = 0
        plane_license_list = self.instance_API.get_list('airplane','plane_licences')
        #plane_license_list = ["hello","world","long"]
        editwin = curses.newwin(len(plane_license_list),20,y,x)
        editwin2 = curses.newwin(1,30,16,67)
        editwin.keypad(1)
        curses.curs_set(0)
        while True:
            if create == 0:
                editwin2.clear()
                editwin2.attron(curses.color_pair(2))
                editwin2.addstr(0,0,plane_license_list[position_y])
                editwin2.attroff(curses.color_pair(2))
                editwin2.refresh()
            editwin.refresh()
            for i in range(len(plane_license_list)):
                if position_y == i:
                    self.license_drop_down(editwin,plane_license_list[i],i,curses.color_pair(2))
                else:
                    self.license_drop_down(editwin,plane_license_list[i],i,curses.color_pair(1))
            button_press = editwin.getch()
            if button_press == curses.KEY_UP or button_press == 450:
                if position_y == 0:
                    position_y = len(plane_license_list)-1
                else:
                    position_y -= 1
            elif button_press == curses.KEY_DOWN or button_press == 456:
                if position_y == len(plane_license_list)-1:
                    position_y = 0
                else:
                    position_y += 1
            elif button_press == 10:
                for i in range(len(plane_license_list)):
                    self.license_drop_down(editwin,"{:^{length:}}".format("",length = 19),i,curses.color_pair(2))
                curses.curs_set(1)
                return plane_license_list[position_y]

    def license_drop_down(self,editwin,license_string,y,color_pair):
        editwin.attron(color_pair)
        editwin.addstr(y,0,license_string)
        editwin.attroff(color_pair)
        editwin.refresh()

    def drop_down(self,editwin,text_string_1,text_string_2,position_y):
        if position_y == 0:
            editwin.attron(curses.color_pair(2))
            editwin.addstr(0,0,text_string_1)
            editwin.attroff(curses.color_pair(2))
            editwin.attron(curses.color_pair(1))
            editwin.addstr(1,0,text_string_2)
            editwin.attroff(curses.color_pair(1))
        else:
            editwin.attron(curses.color_pair(1))
            editwin.addstr(0,0,text_string_1)
            editwin.attroff(curses.color_pair(1))
            editwin.attron(curses.color_pair(2))
            editwin.addstr(1,0,text_string_2)
            editwin.attroff(curses.color_pair(2))

    def get_user_input(self):
        self.print_menu(self.TUI_list, self.highlight_main_list, [0,0],[0,0])
        curses.curs_set(0)
        self.make_text_appear(3,2,"",100)
        curses.curs_set(1)
        if self.menu_select == 0:
            _id = ""
            while True:
                ssn = self.make_user_input_window(5,15,1,1).strip()
                self.errorcheck.set_ssn(ssn)
                error_msg = self.errorcheck.check_ssn()
                if error_msg == True:
                    self.make_text_appear(5,15,ssn,30,2)
                    break
                else:
                    self.make_text_appear(5,15,error_msg,30,2)
                    time.sleep(1)
            
            while True:
                name = self.make_user_input_window(9,10, name = 1)
                self.errorcheck.set_name(name)
                error_msg = self.errorcheck.check_name()
                if error_msg == True:
                    self.make_text_appear(9,10,name,30,2)
                    break
                else:
                    self.make_text_appear(9,10,error_msg,30,2)
                    time.sleep(1)
            while True:
                address = self.make_user_input_window(12,17)
                self.errorcheck.set_address(address)
                error_msg = self.errorcheck.check_address()
                if error_msg == True:
                    self.make_text_appear(12,17,address,30,2)
                    break
                else:
                    self.make_text_appear(12,17,error_msg,30,2)
                    time.sleep(1)
            while True:
                gsm = self.make_user_input_window(16,10,1)
                self.errorcheck.set_cellphone(gsm)
                error_msg = self.errorcheck.check_cellphone()
                if error_msg == True:
                    self.make_text_appear(16,10,gsm,30,2)
                    break
                else:
                    self.make_text_appear(16,10,error_msg,30,2)
                    time.sleep(1)
            while True:
                email = self.make_user_input_window(5,62)
                self.errorcheck.set_mail(email)
                error_msg = self.errorcheck.check_mail()
                if error_msg == True:
                    self.make_text_appear(5,62,email,30,2)
                    break
                else:
                    self.make_text_appear(5,62,error_msg,30,2)
                    time.sleep(1)
            job_title = self.make_drop_down_menu(9,67,"Pilot","Cabincrew")
            self.make_text_appear(9,67,job_title,30,2)
            self.make_text_appear(10,53,"",30)
            if "Pilot" in job_title:
                self.make_text_appear(16,53,"Flugréttindi:",30)
                rank = self.make_drop_down_menu(12,66,"Captain","Co-Pilot")
                self.make_text_appear(12,66,rank,30,2)
                self.make_text_appear(13,66,"",30)
            else:
                rank = self.make_drop_down_menu(12,66,"Flight Service Manager","Flight Attendant")
                self.make_text_appear(12,66,rank,30,2)
                self.make_text_appear(13,66,"",30)
            if "Pilot" in job_title:
                license = self.make_plane_license_dropdown(10,110)
                self.make_text_appear(16,67,license,30,2)
                time.sleep(1)
            else:
                license = ""
            self.instance_API.create("employee",(_id,ssn,name,address,gsm,email,job_title,rank,license))
            self.feedback_screen("{:^{length:}}".format("User has been saved!",length = 100))
            self.item_list = self.instance_API.get_list("employee")
        if self.menu_select == 1:
            curses.curs_set(0)
            time.sleep(1)
            _id = ""
            date = self.calendar_screen()
            self.print_menu(self.TUI_list, self.highlight_main_list, [0,0],[0,0])
            self.make_text_appear(12,19,"KEF",30,2)
            self.make_text_appear(5,16,date,30,2)
            self.make_text_appear(10,16,"Dæmi: 23:59",30,3)
            curses.curs_set(1)
            while True:
                departure_time_out = self.make_user_input_window(9,22, clock = 1)
                self.errorcheck.set_clock(departure_time_out)
                error_msg = self.errorcheck.check_clock()
                if error_msg == True:
                    self.make_text_appear(9,22,departure_time_out,30,2)
                    break
                else:
                    self.make_text_appear(9,22,error_msg,30,2)
                    time.sleep(1)
            self.make_text_appear(10,16,"",30,3)
            #airplane = self.make_plane_license_dropdown(10,110)
            departure = "KEF"
            temp_list = self.instance_API.get_list("destination")
            destination = self.make_list_dropdown(16,18,temp_list,1,1)
            temp_list = self.instance_API.get_list("airplane","available_planes",date +" "+ departure_time_out, destination[0])
            airplane = self.make_list_dropdown(5,62,temp_list,1,1)
            self.instance_API.create("worktrip",(destination[0],date + " " + departure_time_out,airplane[0]))
            self.feedback_screen("{:^{length:}}".format("Worktrip has been saved!",length = 100))
            self.item_list = self.instance_API.get_list("worktrip")
        if self.menu_select == 2:
            _id = ""
            destination_name = self.make_user_input_window(5,23)
            country = self.make_user_input_window(9,10)
            flight_time = self.make_user_input_window(12,14)
            distance_from_iceland = self.make_user_input_window(16,26)
            name_of_contact = self.make_user_input_window(5,70,name = 1)
            contacts_phone = self.make_user_input_window(9,70)
            airport = self.make_user_input_window(12,65)
            self.instance_API.create("destination",(_id,destination_name,country,flight_time,distance_from_iceland,name_of_contact,contacts_phone,airport))
            self.feedback_screen("{:^{length:}}".format("Destination has been saved!",length = 100))
            self.item_list = self.instance_API.get_list("destination")
        if self.menu_select == 3:
            _id = ""
            plane_id = self.make_user_input_window(5,14)
            plane_type = self.make_user_input_window(9,16)
            manufacturer = self.make_user_input_window(12,18)
            sætafjöldi = self.make_user_input_window(16,16)
            name = self.make_user_input_window(5,59)
            self.instance_API.create("airplane",(_id,plane_id,plane_type,manufacturer,sætafjöldi,name))
            self.feedback_screen("{:^{length:}}".format("Airplane has been saved!",length = 100))
            self.item_list = self.instance_API.get_list("airplane")
        self.new_reg_u_input = False
        time.sleep(1)
        time.sleep(2)
        curses.curs_set(0)

    def calendar_screen(self,time_travel = 0):
        cal = calendar.Calendar()
        editwin2 = curses.newwin(15,100,5,3)
        editwin2.attron(curses.color_pair(1))
        editwin2.keypad(1)
        add_month = 0
        add_year = 0
        datetime_year = datetime.date.today().year
        datetime_month = datetime.date.today().month
        datetime_day = datetime.date.today().day
        starting_day, starting_month, starting_year = datetime_day,datetime_month,datetime_year
        date_selected = 1
        years_added = 0
        while True:
            if  int(datetime_month) + add_month == 13:
                datetime_month = 1
                add_month = 0
                datetime_year += 1
            elif int(datetime_month) + add_month == 0:
                datetime_month = 12
                add_month = 0
                datetime_year -= 1
            month = cal.monthdatescalendar(year = (int(datetime_year)),month = (int(datetime_month) + add_month))
            for i in range(len(month)):
                for x in range(len(month[i])):
                    month[i][x] = str(month[i][x])
            y = 0
            days_in_month = 0
            stop = 0
            editwin2.clear()
            for i in range(len(month)):
                for x in range(len(month[i])):
                    if int(month[i][x][5:7]) == int(datetime_month) + add_month and int(month[i][x][0:4]) == int(datetime_year):
                        days_in_month += 1
                        if date_selected == days_in_month:
                            editwin2.attron(curses.color_pair(2))
                            editwin2.attroff(curses.color_pair(1))
                            selected_day = month[i][x]
                        if stop == 0:
                            editwin2.addstr(y,0,month[i][x])
                            stop = 1
                        elif stop == 1:
                            editwin2.addstr(y,25,month[i][x])
                            stop = 2
                        elif stop == 2:
                            editwin2.addstr(y,50,month[i][x])
                            stop = 3
                        else:
                            editwin2.addstr(y,75,month[i][x])
                            y+=2
                            stop = 0
                        editwin2.attroff(curses.color_pair(2))
                        editwin2.attron(curses.color_pair(1))
            editwin3 = curses.newwin(3,50,21,50)
            editwin3.attron(curses.color_pair(2))
            editwin3.addstr(0,0,"Örvar til að velja dag")
            editwin3.addstr(1,0,"pg up til að fara í næsta mánuð")
            editwin3.addstr(2,0,"pg dn til að fara í seinasta mánuð")
            editwin3.refresh()
            editwin3.attron(curses.color_pair(2))
                        
            check = editwin2.getch()
            if check == curses.KEY_LEFT or check == 452:
                if date_selected == 1 or date_selected == 5 or date_selected == 9  or date_selected == 13  or date_selected == 17 or date_selected == 21 or date_selected == 25 or date_selected == 29:
                    pass
                else:
                    date_selected -= 1
            elif check == curses.KEY_RIGHT or check == 454:
                if date_selected == 4 or date_selected == 8 or date_selected == 12 or date_selected == 16 or date_selected == 20 or date_selected == 24 or date_selected == 28 or date_selected == days_in_month:
                    pass
                else:
                    date_selected += 1
            elif check == curses.KEY_UP or check == 450:
                current = date_selected
                if date_selected == 1 or date_selected == 2 or date_selected == 3 or date_selected == 4:
                    pass
                else:
                    date_selected -= 4
            elif check == curses.KEY_DOWN or check == 456:
                if days_in_month == 31:
                    if date_selected == 28 or date_selected == 29 or date_selected == 30 or date_selected == 31:
                        pass
                    else:
                        date_selected += 4
                elif days_in_month == 30:
                    if date_selected == 28 or date_selected == 29 or date_selected == 30 or date_selected == 27:
                        pass
                    else:
                        date_selected += 4
                elif days_in_month == 29:
                    if date_selected == 28 or date_selected == 29 or date_selected == 26 or date_selected == 27:
                        pass
                    else:
                        date_selected += 4
                elif days_in_month == 28:
                    if date_selected == 28 or date_selected == 25 or date_selected == 26 or date_selected == 27:
                        pass
                    else:
                        date_selected += 4
            elif check == 27:
                editwin2.clear()
                return ""
            elif check == 10:
                editwin2.clear()
                return selected_day
            if time_travel == 0:
                if check == 338:
                    if starting_year + 2 == datetime_year and datetime_month + add_month == 12:
                        pass
                    else:
                        add_month += 1
                        date_selected = 1
                elif check == 339:
                    if starting_year == datetime_year and starting_month == datetime_month:
                        pass
                    else:
                        add_month -= 1
                        date_selected = 1
            elif time_travel == 1:
                if check == 338:
                    if starting_year + 2 == datetime_year and datetime_month + add_month == 12:
                        pass
                    else:
                        add_month += 1
                        date_selected = 1
                elif check == 339:
                    if starting_year - 2 == datetime_year and datetime_month + add_month == 1:
                        pass
                    else:
                        add_month -= 1
                        date_selected = 1

        editwin2.attroff(curses.color_pair(1))
        editwin2.refresh()

    def make_user_input_window(self,y,x, only_num = 0, ssn = 0, clock = 0, name = 0,data = ""):
        editwin = curses.newwin(1,30,y,x)
        editwin.attron(curses.color_pair(2))
        editwin.refresh()
        editwin.addstr(0,0,data)
        #editwin.encoding
        #data = ""
        while True: #This while loop was made to create a custom str input that accepts icelandic chrs, the built in str input for curses only does ascci
            if ssn == 1 and len(data) == 10:
                break
            if len(data) == 29:
                break
            ch = editwin.getch()
            if ch== 10:
                break
            elif ch == 8 or ch == 127:
                data = data[:-1]
            elif data == 27:
                wrapper(main)
            if only_num == 1:
                if ch >=48 and ch <= 57:
                    data += chr(ch)
            elif clock == 1:
                if (ch >= ord("0") and ch <= ord("9")) or ch == ord(":"):
                    data += chr(ch)
            elif name == 1:
                if  (ch >=ord("A") and ch <= ord("Z")) or (ch >=ord("a") and ch <= ord("z"))\
                or ch == ord("é") or ch == ord("É")  or ch == ord("Í") or ch == ord("í") or ch == ord("ó")\
                or ch == ord("Ó") or ch == ord("ý") or ch == ord("Ý") or ch == ord("ú") or ch == ord("Ú") or ch == ord("ð") \
                or ch == ord("Ð") or ch == ord("æ") or ch == ord("Æ") or ch == ord("þ") or ch == ord("Þ")  \
                or ch == ord(" ") or ch == ord("á") or ch == ord("Á") or ch == ord("ö") or ch == ord("Ö"): #This defines all the chrs this custom input accepts
                    data += chr(ch)
            else:
                if (ch >=ord("0") and ch <= ord("9")) or (ch >=ord("@") and ch <= ord("Z")) or (ch >=ord("a") and ch <= ord("z"))\
                or ch == ord("é") or ch == ord("É") or ch == ord(".") or ch == ord("Í") or ch == ord("í") or ch == ord("ó")\
                or ch == ord("Ó") or ch == ord("ý") or ch == ord("Ý") or ch == ord("ú") or ch == ord("Ú") or ch == ord("ð") \
                or ch == ord("Ð") or ch == ord("æ") or ch == ord("Æ") or ch == ord("þ") or ch == ord("Þ") or ch == ord("_") \
                or ch == ord(":") or ch == ord(" ") or ch == ord("á") or ch == ord("Á") or ch == ord("ö") or ch == ord("Ö"): #This defines all the chrs this custom input accepts
                    data += chr(ch)
            editwin.clear()
            editwin.refresh()
            editwin.addstr(0,0,data)
            
        editwin.attroff(curses.color_pair(2))
        return data

    def make_text_appear(self,y,x,text_string,box_len, color_pair = 1):
        editwin2 = curses.newwin(1,box_len,y,x)
        editwin2.attron(curses.color_pair(color_pair))
        editwin2.addstr(text_string)
        editwin2.attroff(curses.color_pair(color_pair))
        editwin2.refresh()

    def feedback_screen(self,text_string):
        editwin2 = curses.newwin(15,100,5,3)
        editwin2.attron(curses.color_pair(1))
        editwin2.addstr(6,0,text_string)
        editwin2.attroff(curses.color_pair(1))
        editwin2.refresh()

    def look_at_specific_unit(self):
        self.print_menu(self.TUI_list, self.highlight_main_list, [0,0],[0,0])
        self.make_text_appear(3,2,"",100)
        self.make_text_appear(21,68,"┌────────┐",12)
        self.make_text_appear(22,68,"|",12)
        self.make_text_appear(22,69," B",12,2)
        self.make_text_appear(22,71,"reyta |",12)
        self.make_text_appear(23,68,"└────────┘",12)
        self.make_text_appear(21,79,"┌──────────────┐",17)
        if self.menu_select == 0:
            self.make_text_appear(22,79,"|",17)
            self.make_text_appear(22,80," V",12,2)
            self.make_text_appear(22,82,"innuyfirlit |",17)
            self.make_text_appear(23,79,"└──────────────┘",17)
            self.make_text_appear(5,4,self._header[self.menu_select][0] + ": " +self.item_list[self.list_line_index+self.next_section][1],49)
            self.make_text_appear(9,4,self._header[self.menu_select][1] + ": " +self.item_list[self.list_line_index+self.next_section][2],49)
            self.make_text_appear(12,4,self._header[self.menu_select][2] + ": " +self.item_list[self.list_line_index+self.next_section][3],49)
            self.make_text_appear(16,4,self._header[self.menu_select][3] + ": " +self.item_list[self.list_line_index+self.next_section][4],49)
            self.make_text_appear(5,53,self._header[self.menu_select][4] + ": " +self.item_list[self.list_line_index+self.next_section][5],49)
            self.make_text_appear(9,53,self._header[self.menu_select][5] + ": " +self.item_list[self.list_line_index+self.next_section][6],49)
            self.make_text_appear(12,53,self._header[self.menu_select][6] + ": " +self.item_list[self.list_line_index+self.next_section][7],49)
            if self.item_list[self.list_line_index+self.next_section][6] == "Pilot":
                self.make_text_appear(16,53,self._header[self.menu_select][7] + ": " +self.item_list[self.list_line_index+self.next_section][8],49)
            else:
                self.make_text_appear(16,53,"",49)
        if self.menu_select == 1:
            self.make_text_appear(5,4,self._header[self.menu_select][0] + ": " +self.item_list[self.list_line_index+self.next_section][1],49)
            self.make_text_appear(7,4,self._header[self.menu_select][1] + ": " +self.item_list[self.list_line_index+self.next_section][2],49)
            self.make_text_appear(9,4,self._header[self.menu_select][2] + ": " +self.item_list[self.list_line_index+self.next_section][3],49)
            self.make_text_appear(11,4,self._header[self.menu_select][3] + ": " +self.item_list[self.list_line_index+self.next_section][4],49)
            self.make_text_appear(12,4,"",49)
            self.make_text_appear(13,4,self._header[self.menu_select][4] + ": " +self.item_list[self.list_line_index+self.next_section][5],49)
            self.make_text_appear(15,4,self._header[self.menu_select][5] + ": " +self.item_list[self.list_line_index+self.next_section][6],49)
            self.make_text_appear(16,4,"",49)
            self.make_text_appear(17,4,self._header[self.menu_select][6] + ": " +self.item_list[self.list_line_index+self.next_section][7],49)
            self.make_text_appear(5,53,self._header[self.menu_select][7] + ": " +self.item_list[self.list_line_index+self.next_section][8],49)
            self.make_text_appear(7,53,self._header[self.menu_select][8] + ": " +self.item_list[self.list_line_index+self.next_section][9],49)
            self.make_text_appear(9,53,self._header[self.menu_select][9] + ": " +self.item_list[self.list_line_index+self.next_section][10],49)
            self.make_text_appear(11,53,self._header[self.menu_select][10] + ": " +self.item_list[self.list_line_index+self.next_section][11],49)
            self.make_text_appear(12,53,"",49)
            self.make_text_appear(13,53,self._header[self.menu_select][11] + ": " +self.item_list[self.list_line_index+self.next_section][12],49)
            self.make_text_appear(15,53,self._header[self.menu_select][12] + ": " +self.item_list[self.list_line_index+self.next_section][13],49)
            self.make_text_appear(16,53,"",49)

        if self.menu_select == 2:
            self.make_text_appear(5,4,self._header[self.menu_select][0] + ": " +self.item_list[self.list_line_index+self.next_section][1],49)
            self.make_text_appear(9,4,self._header[self.menu_select][1] + ": " +self.item_list[self.list_line_index+self.next_section][2],49)
            self.make_text_appear(12,4,self._header[self.menu_select][2] + ": " +self.item_list[self.list_line_index+self.next_section][3],49)
            self.make_text_appear(16,4,self._header[self.menu_select][3] + ": " +self.item_list[self.list_line_index+self.next_section][4],49)
            self.make_text_appear(5,53,self._header[self.menu_select][4] + ": " +self.item_list[self.list_line_index+self.next_section][5],49)
            self.make_text_appear(9,53,self._header[self.menu_select][5] + ": " +self.item_list[self.list_line_index+self.next_section][6],49)
            self.make_text_appear(12,53,self._header[self.menu_select][6] + ": " +self.item_list[self.list_line_index+self.next_section][7],49)
            self.make_text_appear(16,53,"",49)

        if self.menu_select == 3:
            self.make_text_appear(5,4,self._header[self.menu_select][0] + ": " +self.item_list[self.list_line_index+self.next_section][1],49)
            self.make_text_appear(9,4,self._header[self.menu_select][1] + ": " +self.item_list[self.list_line_index+self.next_section][2],49)
            self.make_text_appear(12,4,self._header[self.menu_select][2] + ": " +self.item_list[self.list_line_index+self.next_section][3],49)
            self.make_text_appear(16,4,self._header[self.menu_select][3] + ": " +self.item_list[self.list_line_index+self.next_section][4],49)
            self.make_text_appear(5,53,self._header[self.menu_select][4] + ": " +self.item_list[self.list_line_index+self.next_section][5],49)
            self.make_text_appear(9,53,"",49)
            self.make_text_appear(12,53,"",49)
            self.make_text_appear(16,53,"",49)

        action = self.stdscr.getch()
        if action == ord("b"):
            self.change_user_menu()
        if action == ord("v"):
            if self.menu_select == 0:
                date = self.calendar_screen()
                for i in range(3):
                    self.make_text_appear(21+i,50,"",40)
                staff_schedule = self.instance_API.get_list("worktrip","work_schedule",date,self.item_list[self.list_line_index+self.next_section][0])
                for i in range(15):
                    self.make_text_appear(5+i,3,"",100)
                header_list = ["Brottför","Áfangastaður","Dagsetning",self.item_list[self.list_line_index+self.next_section][2]]
                z = 0
                for i in range(len(header_list)):
                    if i != 3:
                        self.make_text_appear(3,5+z,header_list[i],30)
                    else:
                        self.make_text_appear(3,5+z,header_list[i],30,2)
                    z += 20
                for i in range(len(staff_schedule)):
                    z = 0
                    for x in range(len(staff_schedule)):
                        self.make_text_appear(5+i,5+z,staff_schedule[i][x],30)
                        z += 20
                while True:
                    check = self.stdscr.getch()
                    if check == 27:
                        break
    
    def change_user(self,index,y_position,extra_len, only_num = 0, name = 0, clock = 0):
        check = self.get_chr_from_user(y_position,2 + len(self._header[self.menu_select][index] + self.item_list[self.list_line_index+self.next_section][index+1]) + extra_len)
        variable_x = ""
        while True:
            if check == 8 or check == 127:
                variable_x = self.make_user_input_window(y_position,6 + len(self._header[self.menu_select][index]) + extra_len, only_num = only_num, clock = clock, name = name, data = self.item_list[self.list_line_index+self.next_section][index+1][:-1])
                break
            elif check == 330:
                variable_x = self.make_user_input_window(y_position,6 + len(self._header[self.menu_select][index]) + extra_len, only_num = only_num, clock = clock, name = name)
                break
            elif check in [10,456] or check == curses.KEY_DOWN:
                variable_x = self.item_list[self.list_line_index+self.next_section][index+1]
                break
        return variable_x

    def change_user_dropdown(self,index,y_position,extra_len,text_string1, text_string2, only_num = 0):
        check = self.get_chr_from_user(y_position,2 + len(self._header[self.menu_select][index] + self.item_list[self.list_line_index+self.next_section][index+1]) + extra_len)
        if check == 8:
            variable_x = self.make_drop_down_menu(y_position,6+extra_len+len(self._header[self.menu_select][index]),text_string1,text_string2)
            self.make_text_appear(y_position,6+extra_len+len(self._header[self.menu_select][index]),variable_x,30)
            self.make_text_appear(y_position+1,6+extra_len+len(self._header[self.menu_select][index]),"",30)
        else:
            variable_x = self.item_list[self.list_line_index+self.next_section][index+1]
        return variable_x
    
    def change_user_dropdown_list(self,index,y,x,object_list,lel = 2,return_list = 0):
        check = self.get_chr_from_user(y,x+2 + len(self._header[self.menu_select][index] + self.item_list[self.list_line_index+self.next_section][index+1]))
        if check == 8:
            variable_x = self.make_list_dropdown(y,x+4 + len(self._header[self.menu_select][index] + self.item_list[self.list_line_index+self.next_section][index+1]),object_list,lel,return_list = return_list)
        else:
            variable_x = self.item_list[self.list_line_index+self.next_section][index+1]
        return variable_x

    def make_list_dropdown(self,y,x,object_list, index = 2, return_list = 0):
        """This method gets all airplane licenses and creates a drop down menu for the user"""
        position_y = 0
        editwin = curses.newwin(len(object_list),20,5,110)
        editwin2 = curses.newwin(1,30,y,x)
        editwin.keypad(1)
        curses.curs_set(0)
        while True:
            editwin2.clear()
            editwin2.attron(curses.color_pair(2))
            editwin2.addstr(0,0,object_list[position_y][index])
            editwin2.attroff(curses.color_pair(2))
            editwin2.refresh()
            editwin.refresh()
            for i in range(len(object_list)):
                if position_y == i:
                    self.license_drop_down(editwin,object_list[i][index],i,curses.color_pair(2))
                else:
                    self.license_drop_down(editwin,object_list[i][index],i,curses.color_pair(1))
            button_press = editwin.getch()
            if button_press == curses.KEY_UP or button_press == 450:
                if position_y == 0:
                    position_y = len(object_list)-1
                else:
                    position_y -= 1
            elif button_press == curses.KEY_DOWN or button_press == 456:
                if position_y == len(object_list)-1:
                    position_y = 0
                else:
                    position_y += 1
            elif button_press == 10:
                for i in range(len(object_list)):
                    self.license_drop_down(editwin,"{:^{length:}}".format("",length = 19),i,curses.color_pair(2))
                curses.curs_set(1)
                if return_list == 0:
                    return object_list[position_y][index]
                else:
                    return object_list[position_y]

    def change_user_menu(self):
        if self.menu_select == 0:
            _id = self.item_list[self.list_line_index+self.next_section][0]
            ssn = self.item_list[self.list_line_index+self.next_section][1]
            name = self.item_list[self.list_line_index+self.next_section][2]
            address = self.change_user(2,12,0)
            phone = self.change_user(3,16,0,only_num = 1)
            email = self.change_user(4,5,49)
            job_title = self.item_list[self.list_line_index+self.next_section][6]
            if self.item_list[self.list_line_index+self.next_section][6] == "Pilot":
                rank = self.change_user_dropdown(6,12,49,"Captain","Co-Pilot")
                license = self.change_user(7,16,49)
            else:
                rank = self.change_user_dropdown(6,12,49,"Flight Service Manager","Flight Attendant")
                license = ""
            self.instance_API.change("employee",(_id,ssn,name,address,phone,email,job_title,rank,license))
            self.item_list = self.instance_API.get_list("employee")

        if self.menu_select == 1:
            while True:
                #change_user(self,index,y_position,extra_len, only_num = 0):
                _id = self.item_list[self.list_line_index+self.next_section][0]
                flight_number_out = self.item_list[self.list_line_index+self.next_section][1]
                flight_number_home = self.item_list[self.list_line_index+self.next_section][2]
                departing_from = self.item_list[self.list_line_index+self.next_section][3]
                arriving_at = self.change_user(3,11,0)
                departure = self.change_user(4,13,0)
                arrival = self.change_user(5,15,0)
                departure_split = departure.split(" ")
                dest_id = self.instance_API.get_list('destination',"destination_id",arriving_at)
                temp_list = self.instance_API.get_list("airplane","available_planes",departure, dest_id)
                aircraft_id = self.change_user_dropdown_list(6,17,0,temp_list,1)
                temp_list = self.instance_API.get_list("worktrip", "available_employees",departure_split[0].strip(), rank='Captain', a_license=aircraft_id)
                try:
                    captain = self.change_user_dropdown_list(7,5,49,temp_list,2)
                except:
                    self.feedback_screen("{:^{length:}}".format("Enginn laus captain með réttindi á vélina",length = 100))
                    time.sleep(5)
                    break
                temp_list = self.instance_API.get_list("worktrip", "available_employees",departure_split[0],role='Pilot', a_license=aircraft_id)
                for i in range(len(temp_list)):
                        if captain in temp_list[i]:
                            temp_list.pop(i)
                            break
                copilot = self.change_user_dropdown_list(8,7,50,temp_list,return_list = 1)
                temp_list = self.instance_API.get_list('worktrip',"available_employees",departure_split[0],rank = "Flight Service Manager")
                fsm = self.change_user_dropdown_list(9,9,49,temp_list)
                temp_list = self.instance_API.get_list('worktrip',"available_employees",departure_split[0],role = "Cabincrew")
                for i in range(len(temp_list)):
                        if fsm in temp_list[i]:
                            temp_list.pop(i)
                            break
                fa1 = self.change_user_dropdown_list(10,11,49,temp_list)
                for i in range(len(temp_list)):
                        if fa1 in temp_list[i]:
                            temp_list.pop(i)
                            break
                fa2 = self.change_user(11,13,49,temp_list)

        if self.menu_select == 2:
            _id = self.item_list[self.list_line_index+self.next_section][0]
            name = self.change_user(0,5,0)
            country = self.change_user(1,9,0)
            flight_time = self.change_user(2,12,0)
            distance_from_iceland = self.change_user(3,16,0)
            emergency_contact = self.change_user(4,5,49)
            emergency_contact_phonenr = self.change_user(5,9,49,1)
            airport = self.change_user(6,12,49)

        if self.menu_select == 3:
            _id = self.item_list[self.list_line_index+self.next_section][0]
            plane_id = self.change_user(1,5,0)
            plane_type = self.change_user(2,9,0)
            manufacturer = self.change_user(3,12,0)
            seat_amount = self.change_user(4,16,0)
            name = self.change_user(5,5,49)
            

    def get_chr_from_user(self,y,x):
        editwin = curses.newwin(1,1,y,4+x)
        editwin.keypad(1)
        editwin.attron(curses.color_pair(2))
        curses.curs_set(1)
        editwin.refresh()
        editwin.attroff(curses.color_pair(2))
        return editwin.getch()

    def make_special_search(self):
        pass

    def main(self):
        # Clear screen
        self.stdscr.clear() 
        curses.init_color(1, 0, 0, 0)
        curses.can_change_color()
        curses.init_color(curses.COLOR_GREEN,1000,0,0)
        curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
        curses.init_pair(2,curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3,curses.COLOR_WHITE, curses.COLOR_BLACK)
        
        # This raises ZeroDivisionError when i == 10.
        idx = 0
        idy = 0
        idz = 0
        list_den = [[1,1],[1,3],[1,5],[1,7]]
        list_den2 = [[3,1],[3,2],[3,3],[3,4],[3,5]]
        list_den3 = [[5,1],[6,1],[7,1],[8,1],[9,1],[10,1],[11,1],[12,1],[13,1],[14,1],[15,1],[16,1],[17,1],[18,1],[19,1],[20,1]]
        list_den4 = [[[22,4,"S"],[22,14,"N"],[22,24,"D"],[22,38,"F"]],[[22,4,"S"],[22,14,"N"],[22,24,"D"],[22,38,"V"]],[[22,4,"S"],[22,14,"N"]],[[22,4,"S"],[22,14,"N"],[22,24,"D"]]]
        
        while True:
            TUI_list = self.construct_TUI(self.highlight_main_list)
            x = 4
            y = 10
            self.print_menu(TUI_list, list_den[idx], list_den3[idz],list_den4[idx])
            if self.exeption == 1:
                self.make_text_appear(21,65,"Flokka eftir ",20)
                self.make_text_appear(21,78,"L",2,2)
                self.make_text_appear(21,79,"eyfum",10)
                self.make_text_appear(22,65,"Flokka eftir ",20)
                self.make_text_appear(22,78,"T",2,2)
                self.make_text_appear(22,79,"itil",10)
            if self.exeption == 2:
                self.make_text_appear(22,65,"Flokka eftir ",20)
                self.make_text_appear(22,78,"T",2,2)
                self.make_text_appear(22,79,"itil",10)
            #string_input = stdscr.getstr(21, 70)
            if self.new_reg_u_input == True:
                self.get_user_input()
                key = 0
            elif self.check_specifcly == True:
                self.look_at_specific_unit()
                key = 0
                self.check_specifcly = False
            else:
                curses.curs_set(0)
                curses.noecho()
                self.stdscr.refresh()
                key = self.stdscr.getch()
            if key == 49:
                self.menu_select = 0
                self.exeption = 0
                self.next_section = 0
                idx = 0
                idz = 0
                self.item_list = self.instance_API.get_list("employee")
                """leng = 0
                for i in range(len(self.item_list)):
                    for x in range(len(self.item_list[i])):
                        self.stdscr.attron(curses.color_pair(1))
                        self.stdscr.addstr(0,leng,self.item_list[i][x]+" ")
                        self.stdscr.attroff(curses.color_pair(1))
                        self.stdscr.refresh()
                        leng += len(self.item_list[i][x]) +1 
                    time.sleep(1)
                    leng = 0"""
            elif key == 50:
                self.menu_select = 1
                self.next_section = 0
                idx = 1
                idz = 0
                self.item_list = self.instance_API.get_list("worktrip")
                """leng = 0
                for i in range(len(self.item_list)):
                    for x in range(len(self.item_list[i])):
                        self.stdscr.attron(curses.color_pair(1))
                        self.stdscr.addstr(0,leng,self.item_list[i][x]+" ")
                        self.stdscr.attroff(curses.color_pair(1))
                        self.stdscr.refresh()
                        leng += len(self.item_list[i][x]) +1 
                    time.sleep(1)
                    leng = 0"""
            elif key == 51:
                self.menu_select = 2
                self.next_section = 0
                idx = 2
                idz = 0
                self.item_list = self.instance_API.get_list("destination")
                """leng = 0
                for i in range(len(self.item_list)):
                    for x in range(len(self.item_list[i])):
                        self.stdscr.attron(curses.color_pair(1))
                        self.stdscr.addstr(0,leng,self.item_list[i][x]+" ")
                        self.stdscr.attroff(curses.color_pair(1))
                        self.stdscr.refresh()
                        leng += len(self.item_list[i][x]) +1 
                    time.sleep(1)
                    leng = 0"""
            elif key == 52:
                self.menu_select = 3
                self.next_section = 0
                idx = 3
                idz = 0
                self.item_list = self.instance_API.get_list("airplane")
                """leng = 0
                for i in range(len(self.item_list)):
                    for x in range(len(self.item_list[i])):
                        self.stdscr.attron(curses.color_pair(1))
                        self.stdscr.addstr(0,leng,self.item_list[i][x]+" ")
                        self.stdscr.attroff(curses.color_pair(1))
                        self.stdscr.refresh()
                        leng += len(self.item_list[i][x]) +1 
                    time.sleep(1)
                    leng = 0"""
            elif key == curses.KEY_LEFT or key == 452:
                if self.next_section == 0:
                    self.next_section = 0
                    self.list_line_index = 0
                    idz = 0
                else:
                    self.next_section -= 15
                    self.list_line_index = 0
                    idz = 0
            elif key == curses.KEY_RIGHT or key == 454:
                if self.next_section < len(self.item_list) - 15:
                    self.next_section += 15
                    self.list_line_index = 0
                    idz = 0
                
            elif key == curses.KEY_UP or key == 450:
                if idz == 0:
                    idz = self.select_len-1
                    self.list_line_index = self.select_len-1
                else:
                    idz -= 1
                    self.list_line_index -= 1
            elif key == curses.KEY_DOWN or key == 456:
                if idz == self.select_len-1:
                    idz = 0
                    self.list_line_index = 0
                else:
                    idz += 1
                    self.list_line_index += 1
            elif key == 27:
                break
            elif key == ord("v"):
                if self.menu_select == 1:
                    date = self.calendar_screen()
                    new_list = self.instance_API.get_list("worktrip","work_schedule",date)
                    if not new_list:
                        self.feedback_screen("{:^{length:}}".format("Engar vinnuferðir í þessari viku!",length = 100))
                        time.sleep(3)
                    else:
                        self.item_list = new_list
            elif key == ord("n"):
                self.new_registration = True
                self.new_reg_u_input = True
            elif key == ord("s") or key == 10:
                self.check_specifcly = True
            elif key == ord("d"):
                if self.menu_select == 0:
                    while True:
                        self.make_text_appear(21,23,"|",3)
                        self.make_text_appear(21,24,"L",3,2)
                        self.make_text_appear(21,25,"ausir   |",11)
                        self.make_text_appear(22,23,"|",3,)
                        self.make_text_appear(22,24,"U",3,2)
                        self.make_text_appear(22,25,"ppteknir|",11)
                        self.make_text_appear(23,23,"|",12,1)
                        self.make_text_appear(23,24,"Esc     ",12,2)
                        self.make_text_appear(23,27,"      |",8,1)
                        option = self.stdscr.getch()
                        self.make_text_appear(21,23,"|",3)
                        self.make_text_appear(21,24,"V",3,2)
                        self.make_text_appear(21,25,"ika      |",11)
                        self.make_text_appear(22,23,"|",3,)
                        self.make_text_appear(22,24,"D",3,2)
                        self.make_text_appear(22,25,"agsetning|",11)
                        self.make_text_appear(23,23,"|",12,1)
                        self.make_text_appear(23,24,"Esc     ",12,2)
                        self.make_text_appear(23,27,"      |",8,1)
                        if option == 27:
                            break
                        elif option == ord("l") or option == ord("u"):
                            date = self.calendar_screen()
                            if option == ord("l"):
                                self.item_list  = self.instance_API.get_list(keyword = 'worktrip', list_type = 'available_employees', searchparam = date)
                                break    
                            if option == ord("u"):
                                self.item_list  = self.instance_API.get_list('worktrip', list_type = 'working_employees', searchparam = date)
                                break
                if self.menu_select == 1:
                    date = self.calendar_screen()
                    new_list = self.instance_API.get_list("worktrip","work_schedule",date,"", days = 1)
                    if not new_list:
                        self.feedback_screen("{:^{length:}}".format("Engar vinnuferðir á þessum degi!",length = 100))
                        time.sleep(3)
                    else:
                        self.item_list = new_list
            elif self.menu_select == 0:
                self.item_list = self.instance_API.get_list("employee")
                if key == ord("f"):
                    self.list_line_index = 0
                    idz = 0
                    buffer_str = self.highlight_main_list.pop()
                    self.highlight_main_list.insert(0,buffer_str)
                    if self.exeption != 2:
                        self.exeption += 1
                    else:
                        self.exeption = 0
                    if self.exeption == 1:
                        buffer_list = []
                        for i in range(len(self.item_list)):
                            if "Pilot" in self.item_list[i]:
                                buffer_list.append(self.item_list[i])
                        self.item_list = buffer_list
                    if self.exeption == 2:
                        buffer_list = []
                        for i in range(len(self.item_list)):
                            if "Cabincrew" in self.item_list[i]:
                                buffer_list.append(self.item_list[i])
                        self.item_list = buffer_list
                elif self.exeption == 1 and key == ord("l"):
                    self.list_line_index = 0
                    idz = 0
                    license = self.make_plane_license_dropdown(10,110,1)
                    buffer_list = []
                    for i in range(len(self.item_list)):
                        if license in self.item_list[i]:
                            buffer_list.append(self.item_list[i])
                    self.item_list = buffer_list
                elif (self.exeption == 1 or self.exeption == 2) and key == ord("t"):
                    self.list_line_index = 0
                    idz = 0
                    if self.exeption2 != 2:
                        self.exeption2 += 1
                    else:
                        self.exeption2 = 0
                    if self.exeption == 1 and self.exeption2 == 1:
                        buffer_list = []
                        for i in range(len(self.item_list)):
                            if "Captain" in self.item_list[i]:
                                buffer_list.append(self.item_list[i])
                        self.item_list = buffer_list
                    if self.exeption == 1 and self.exeption2 == 2:
                        buffer_list = []
                        for i in range(len(self.item_list)):
                            if "Co-Pilot" in self.item_list[i]:
                                buffer_list.append(self.item_list[i])
                        self.item_list = buffer_list
                    if self.exeption == 2 and self.exeption2 == 1:
                        buffer_list = []
                        for i in range(len(self.item_list)):
                            if "Flight Service Manager" in self.item_list[i]:
                                buffer_list.append(self.item_list[i])
                        self.item_list = buffer_list
                    if self.exeption == 2 and self.exeption2 == 2:
                        buffer_list = []
                        for i in range(len(self.item_list)):
                            if "Flight Attendant" in self.item_list[i]:
                                buffer_list.append(self.item_list[i])
                        self.item_list = buffer_list
                """self.stdscr.clear()
                self.stdscr.attron(curses.color_pair(1))
                self.stdscr.addstr(0,0,str(key))
                self.stdscr.attroff(curses.color_pair(1))
                self.stdscr.refresh()
                time.sleep(1)"""

    def print_menu(self, TUI_list, list_den ,list_den3 ,idx ):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()
        for y in range(len(TUI_list)):
            z = 0
            for x in range(len(TUI_list[y])):
                if y == list_den[0] and x == list_den[1]:
                    self.stdscr.attron(curses.color_pair(2))
                    self.stdscr.addstr(y,z,TUI_list[y][x])
                    self.stdscr.attroff(curses.color_pair(2))
                elif y == list_den3[0] and x == list_den3[1]:
                    if list_den3[0] != 0:
                        self.stdscr.attron(curses.color_pair(2))
                        self.stdscr.addstr(y,z,TUI_list[y][x])
                        self.stdscr.attroff(curses.color_pair(2))
                    else:
                        self.stdscr.attron(curses.color_pair(1))
                        self.stdscr.addstr(y,z,TUI_list[y][x])
                        self.stdscr.attroff(curses.color_pair(1))
                else:
                    self.stdscr.attron(curses.color_pair(1))
                    self.stdscr.addstr(y,z,TUI_list[y][x])
                    self.stdscr.attroff(curses.color_pair(1))
                z += len(TUI_list[y][x])
        if idx[0] != 0:
            for i in range(len(idx)):
                self.stdscr.delch(idx[i][0],idx[i][1])
                self.stdscr.insstr(idx[i][0],idx[i][1],idx[i][2],curses.color_pair(2))
        curses.curs_set(0)
        self.stdscr.refresh()
        
#curses.cbreak
#curses.nocbreak
#time.sleep(1)
#wrapper(main)

def start(stdscr):
    new_tui = TUI(stdscr)
    new_tui.main()
#ég er flottur
#ég er flottari gaur
#ég er flottastur gaur
#ég er ennþá flottastastur gaur
#wrapper(start)