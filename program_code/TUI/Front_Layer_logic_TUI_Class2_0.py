#import User_interface
from LL.LL_API_sigurgeir import *
from LL.LL_API_eythor import *
import os
#import Front_layer_TUI
import locale
import curses
import time
import datetime
import dateutil.parser
import calendar

#from LL.LL_API_eythor import *
from curses import wrapper, color_pair
from curses.textpad import Textbox, rectangle
header_lengd = 20
os.system('mode con: cols=150 lines=30')  # works on M$ Windows
# coding = UTF-8

item_list = [[["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""],
                ["Arnar Ívarsson","Flugþjónn","","Í ferð","New York"],
                ["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""],
                ["Arnar Ívarsson","Flugþjónn","","Í ferð","New York"],
                ["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""],
                ["Arnar Ívarsson","Flugþjónn","","Í ferð","New York"],
                ["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""],
                ["Arnar Ívarsson","Flugþjónn","","Í ferð","New York"],
                ["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""],
                ["Arnar Ívarsson","Flugþjónn","","Í ferð","New York"],
                ["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""],
                ["Arnar Ívarsson","Flugþjónn","","Í ferð","New York"],
                ["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""],
                ["Arnar Ívarsson","Flugþjónn","","Í ferð","New York"],
                ["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""]
                ],
                [["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð","NA011","100/150","Lokið"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð","NA012","104/150","Lokið"],
                ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð","NA011","100/150","Lokið"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð","NA012","104/150","Lokið"],
                ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð","NA011","100/150","Lokið"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð","NA012","104/150","Lokið"],
                ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð","NA011","100/150","Lokið"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð","NA012","104/150","Lokið"],
                ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð","NA011","100/150","Lokið"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð","NA012","104/150","Lokið"],
                ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð","NA011","100/150","Lokið"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð","NA012","104/150","Lokið"],
                ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð","NA011","100/150","Lokið"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð","NA012","104/150","Lokið"],
                ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð","NA011","100/150","Lokið"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð","NA012","104/150","Lokið"],
                ],
                [["Longyearbyen","Svalbarði","Svalbard Airport","Finnur Finnason","2342342342"],
                ["Berlín","Þýskaland","Berlin Airport","Baldur Magnússon","45443788643"],
                ["Longyearbyen","Svalbarði","Svalbard Airport","Finnur Finnason","2342342342"],
                ["Berlín","Þýskaland","Berlin Airport","Baldur Magnússon","45443788643"],
                ["Longyearbyen","Svalbarði","Svalbard Airport","Finnur Finnason","2342342342"],
                ["Berlín","Þýskaland","Berlin Airport","Baldur Magnússon","45443788643"],
                ["Longyearbyen","Svalbarði","Svalbard Airport","Finnur Finnason","2342342342"],
                ["Berlín","Þýskaland","Berlin Airport","Baldur Magnússon","45443788643"],
                ["Longyearbyen","Svalbarði","Svalbard Airport","Finnur Finnason","2342342342"],
                ["Berlín","Þýskaland","Berlin Airport","Baldur Magnússon","45443788643"],
                ["Longyearbyen","Svalbarði","Svalbard Airport","Finnur Finnason","2342342342"],
                ["Berlín","Þýskaland","Berlin Airport","Baldur Magnússon","45443788643"],
                ["Longyearbyen","Svalbarði","Svalbard Airport","Finnur Finnason","2342342342"],
                ["Berlín","Þýskaland","Berlin Airport","Baldur Magnússon","45443788643"],
                ["Longyearbyen","Svalbarði","Svalbard Airport","Finnur Finnason","2342342342"]
                ],
                [["Batman","Boeing 747","400","Laus","","","12/12/19 - 14:30"],
                ["Spiderman","Boeing 767","500","Lent ytra","New York","NA2020","12/12/19 - 18:20"],
                ["Batman","Boeing 747","400","Laus","","","12/12/19 - 14:30"],
                ["Spiderman","Boeing 767","500","Lent ytra","New York","NA2020","12/12/19 - 18:20"],
                ["Batman","Boeing 747","400","Laus","","","12/12/19 - 14:30"],
                ["Spiderman","Boeing 767","500","Lent ytra","New York","NA2020","12/12/19 - 18:20"],
                ["Batman","Boeing 747","400","Laus","","","12/12/19 - 14:30"],
                ["Spiderman","Boeing 767","500","Lent ytra","New York","NA2020","12/12/19 - 18:20"],
                ["Batman","Boeing 747","400","Laus","","","12/12/19 - 14:30"],
                ["Spiderman","Boeing 767","500","Lent ytra","New York","NA2020","12/12/19 - 18:20"],
                ["Batman","Boeing 747","400","Laus","","","12/12/19 - 14:30"],
                ["Spiderman","Boeing 767","500","Lent ytra","New York","NA2020","12/12/19 - 18:20"],
                ["Batman","Boeing 747","400","Laus","","","12/12/19 - 14:30"],
                ["Spiderman","Boeing 767","500","Lent ytra","New York","NA2020","12/12/19 - 18:20"],
                ["Batman","Boeing 747","400","Laus","","","12/12/19 - 14:30"],
                ["Spiderman","Boeing 767","500","Lent ytra","New York","NA2020","12/12/19 - 18:20"],
                ]
                ]

class TUI():
    def __init__(self,stdscr,highlight_index = 0):
        self.menu_select = 0
        self.exeption = 0
        self.new_registration = False
        self.stdscr = stdscr
        self.new_reg_u_input = False
        self.highlight_main_list = ["x", " ", " "]
        self.highlight_index = highlight_index
        self.list_line_index = 0
        self.check_specifcly = False
        self.item_list1 = []
    def construct_TUI(self,x_list):
        main_menu_temp = self.construct_main_menu()
        header_temp = self.construct_header()
        if self.new_registration == True:
            body_temp = self.construct_body_new_registration()
        elif self.check_specifcly == True:
            body_temp = self.construct_body_new_registration()
        else:    
            body_temp = self.construct_body_lists()
        
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

    def construct_header(self):
        self.header = (\
        ("Nafn","Starf","Réttindi","Staða","Áfangastaður"),\
        ("Dagsetning","Brottför","Áfangastaður","Flugvél","Mönnun","Flugnr.","Sæti","Staða"),\
        ("Nafn","Land","FlugVöllur","Tengiliður","Sími"),\
        ("Nafn","Tegund","Sæti","Staða","Áfangastaður","Flugnr.","Aflögufær"))
        header_string = ""
        for i in range(len(self.header[self.menu_select])):
            header_string += "{:<{lengd:}}".format(self.header[self.menu_select][i],lengd = int(100/(len(self.header[self.menu_select]))))
        for i in range(100-len(header_string)):
            header_string += " "
        header_template = (
        (("║  "),(header_string),("  ║")),
        )
        return header_template

    def construct_body_lists(self):
        new_list = []
        exeptions = ["", "Flugmaður", "Flugþjónn"]
        for i in range(len(item_list[self.menu_select])):
            new_string = ""
            if self.menu_select == 0:
                if exeptions[self.exeption] in item_list[self.menu_select][i]:
                    for x in range(len(item_list[self.menu_select][i])):
                        new_string += "{:<{lengd:}}".format(item_list[self.menu_select][i][x],lengd = int(100/(len(item_list[self.menu_select][i]))))
                    new_list.append(new_string)
            else:
                for x in range(len(item_list[self.menu_select][i])):
                    new_string += "{:<{lengd:}}".format(item_list[self.menu_select][i][x],lengd = int(100/(len(item_list[self.menu_select][i]))))
                new_list.append(new_string)
        for i in range(15-len(new_list)):
            new_list.append("{:^{lengd:}}".format("", lengd = 100))
        for i in range(len(new_list)):
            for x in range(100-len(new_list[i])):
                new_list[i] += " "
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
        registration_list = (
            ("Kennitala:","Nafn:","Heimilsfang:","Gsm sími:", "Netfang:","Starfstitill:","Starfsstaða:"),
            ("Dagsetning:","Brottfaratími út:","Flugvél:","Upphafsstaður:","Áfangastaður:"),
            ("Nafn áfangastaðar:","Land:", "Flugvöllur:","Flugtími:","Fjarlægð frá Íslandi:", "Nafn tengiliðar:","Neyðarsímanúmer:"),
            ("Nafn:","Framleiðandi:","Tengund:","Fjöldi sæta:"),
            )
        new_list = []
        exeptions = ["", "Flugmaður", "Flugþjónn"]
        new_string = ""
        for i in range(len(registration_list[self.menu_select])):
            new_string += "{:<{lengd:}}".format(registration_list[self.menu_select][i],lengd = 49)
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

    def construct_footer(self, x_list):
        top_box = "┌───────┐"
        top_box2 = "┌──────────┐"
        top_box3 = "┌────────┐"
        bot_box = "└───────┘"
        bot_box2 = "└──────────┘"
        bot_box3 = "└────────┘"
        check_box_left = " ("
        check_box_right = ")"
        check_box_x = x_list
        one_space_string = "  "
        empty_string1 = "     "
        empty_string2 = "         "
        Flokka_listi = [[
        " {:<{lengd:}}".format("Allir",lengd = 12),
        " {:<{lengd:}}".format("Flugmenn",lengd = 12),
        " {:<{lengd:}}".format("Flugþjónar",lengd = 12),
        ],
        [
        " {:<{lengd:}}".format("",lengd = 15),
        ]
        ]
        footer = (
        (
        (top_box,top_box3,top_box2,top_box3, check_box_left + check_box_x[0] + check_box_right + Flokka_listi[0][0]),
        (
        "{:^{lengd:}}".format("| Skoða |",lengd = 9),\
        "{:^{lengd:}}".format("| Nýskrá |",lengd = 10),\
        "{:^{lengd:}}".format("|Dagsetning|",lengd = 12),\
        "{:^{lengd:}}".format("| Flokka |",lengd = 10),
        check_box_left + check_box_x[1] + check_box_right + Flokka_listi[0][1]
        ),
        (bot_box,bot_box3,bot_box2,bot_box3,check_box_left + check_box_x[2] + check_box_right + Flokka_listi[0][2])
        ),
        (
        (top_box,top_box3,top_box2,top_box, one_space_string + Flokka_listi[1][0]),
        (
        "{:^{lengd:}}".format("| Skoða |",lengd = 9),\
        "{:^{lengd:}}".format("| Nýskrá |",lengd = 10),\
        "{:^{lengd:}}".format("|Dagsetning|",lengd = 12),\
        "{:^{lengd:}}".format("| Vika  |",lengd = 9),
        one_space_string + Flokka_listi[1][0]
        ),
        (bot_box,bot_box3,bot_box2,bot_box,one_space_string + Flokka_listi[1][0])
        ),
        (
        (top_box,top_box3,empty_string2,empty_string2, empty_string1 + Flokka_listi[1][0]),
        (
        "{:^{lengd:}}".format("| Skoða |",lengd = 9),\
        "{:^{lengd:}}".format("| Nýskrá |",lengd = 10),\
        "{:^{lengd:}}".format("",lengd = 9),\
        "{:^{lengd:}}".format("",lengd = 9) ,
        empty_string1 + Flokka_listi[1][0]
        ),
        (bot_box,bot_box3,empty_string2,empty_string2,empty_string1 + Flokka_listi[1][0])
        ),
        (
        (top_box,top_box3,top_box2,empty_string2, one_space_string + Flokka_listi[1][0]),
        (
        "{:^{lengd:}}".format("| Skoða |",lengd = 9),\
        "{:^{lengd:}}".format("| Nýskrá |",lengd = 10),\
        "{:^{lengd:}}".format("|Dagsetning|",lengd = 12),\
        "{:^{lengd:}}".format("",lengd = 9) ,
        one_space_string + Flokka_listi[1][0]
        ),
        (bot_box,bot_box3,bot_box2,empty_string2,one_space_string + Flokka_listi[1][0])
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
        self.print_menu(self.TUI_list, self.highlight_main_list[self.highlight_index], [0,0],[0,0])
        curses.curs_set(1)
        if self.menu_select == 0:
            """while True:"""
            kt = self.make_user_input_window(5,15)
            """check,error_msg = Errorcheck.check_ssn(kt.strip())
            if check == True:
                break
            else:
                self.make_text_appear(5,15,error_msg,30)
                time.sleep(1)"""
            name = self.make_user_input_window(9,10)
            address = self.make_user_input_window(12,17)
            gsm = self.make_user_input_window(16,14)
            email = self.make_user_input_window(5,62)
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
                licence = self.make_user_input_window(16,67)
            else:
                licence = ""
            le = (kt,name,address,gsm,email,job_title,rank,licence)
            self.feedback_screen("{:^{length:}}".format("User has been saved!",length = 100))
        if self.menu_select == 1:
            curses.curs_set(0)
            time.sleep(1)
            date = self.calendar_screen()
            self.print_menu(self.TUI_list, self.highlight_main_list[self.highlight_index], [0,0],[0,0])
            self.make_text_appear(16,19,"KEF",30,2)
            self.make_text_appear(5,16,date,30,2)
            self.make_text_appear(10,22,"xx:xx",30,3)
            curses.curs_set(1)
            departure_time_out = self.make_user_input_window(9,22)
            airplane = self.make_user_input_window(12,13)
            destination = self.make_user_input_window(5,67)
            le = (date,departure_time_out,airplane,destination)
            self.feedback_screen("{:^{length:}}".format("Worktrip has been saved!",length = 100))
        if self.menu_select == 2:
            destination_name = self.make_user_input_window(5,23)
            country = self.make_user_input_window(9,10)
            airport = self.make_user_input_window(12,16)
            fly_time = self.make_user_input_window(16,14)
            distance_from_iceland = self.make_user_input_window(5,75)
            name_of_contact = self.make_user_input_window(9,70)
            contacts_phone = self.make_user_input_window(12,70)
            le = (destination_name,country,airport,fly_time,distance_from_iceland,name_of_contact,contacts_phone)
            self.feedback_screen("{:^{length:}}".format("Destination has been saved!",length = 100))
        if self.menu_select == 3:
            name = self.make_user_input_window(5,10)
            producer = self.make_user_input_window(9,18)
            product_id = self.make_user_input_window(12,13)
            num_of_seats = self.make_user_input_window(16,17)
            le = (name,producer,product_id,num_of_seats)
            self.feedback_screen("{:^{length:}}".format("Airplane has been saved!",length = 100))
        self.new_reg_u_input = False
        time.sleep(1)
        time.sleep(2)
        curses.curs_set(0)

    def calendar_screen(self):
            cal = calendar.Calendar()
            editwin2 = curses.newwin(15,100,5,3)
            editwin2.attron(curses.color_pair(1))
            editwin2.keypad(1)
            add_month = 0
            add_year = 0
            datetime_year = datetime.date.today().year
            datetime_month = datetime.date.today().month
            starting_month, starting_year = datetime_month,datetime_year
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
                for i in range(len(month)):
                    for x in range(len(month[i])):
                        if int(month[i][x][5:7]) == int(datetime_month) + add_month and int(month[i][x][0:4]) == int(datetime_year):
                            days_in_month += 1
                            if date_selected == days_in_month:
                                editwin2.attron(curses.color_pair(2))
                                editwin2.attroff(curses.color_pair(1))
                                selected_day = month[i][x]
                            if stop == 0:
                                editwin2.addstr(y,0,month[i][x].strftime("%d %b %Y"))
                                stop = 1
                                if y > 15:
                                    y = 0
                            elif stop == 1:
                                editwin2.addstr(y,25,month[i][x].strftime("%d %b %Y"))
                                stop = 2
                                if y > 15:
                                    
                                    y = 0
                            elif stop == 2:
                                editwin2.addstr(y,50,month[i][x].strftime("%d %b %Y"))
                                stop = 3
                                if y > 15:
                                    
                                    y = 0
                            else:
                                editwin2.addstr(y,75,month[i][x].strftime("%d %b %Y"))
                                y+=2
                                stop = 0
                                if y > 15:
                                    y = 0
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
                if check == curses.KEY_LEFT:
                    if date_selected == 1:
                        pass
                    elif date_selected == 5:
                        pass
                    elif date_selected == 9:
                        pass
                    elif date_selected == 13:
                        pass
                    elif date_selected == 17:
                        pass
                    elif date_selected == 21:
                        pass
                    elif date_selected == 25:
                        pass
                    elif date_selected == 29:
                        pass
                    else:
                        date_selected -= 1
                elif check == curses.KEY_RIGHT:
                    if date_selected == 4:
                        pass
                    elif date_selected == 8:
                        pass
                    elif date_selected == 12:
                        pass
                    elif date_selected == 16:
                        pass
                    elif date_selected == 20:
                        pass
                    elif date_selected == 24:
                        pass
                    elif date_selected == 28:
                        pass
                    elif date_selected == days_in_month:
                        pass
                    else:
                        date_selected += 1
                elif check == curses.KEY_UP or check == 450:
                    current = date_selected
                    if date_selected == 1:
                        pass
                    elif date_selected == 2:
                        pass
                    elif date_selected == 3:
                        pass
                    elif date_selected == 4:
                        pass
                    else:
                        date_selected -= 4
                elif check == curses.KEY_DOWN or check == 456:
                    if date_selected == 28:
                        pass
                    elif date_selected == 29:
                        pass
                    elif date_selected == 30:
                        pass
                    elif date_selected == 31:
                        pass
                    else:
                        date_selected += 4
                elif check == 27:
                    editwin2.clear()
                    return ""
                elif check == 10:
                    editwin2.clear()
                    return selected_day
                elif check == 338:
                    if starting_year + 2 == datetime_year and datetime_month + add_month == 12:
                        pass
                    else:
                        add_month += 1
                elif check == 339:
                    if starting_year == datetime_year and starting_month == datetime_month:
                        pass
                    else:
                        add_month -= 1

            editwin2.attroff(curses.color_pair(1))
            editwin2.refresh()

    def make_user_input_window(self,y,x):
        editwin = curses.newwin(1,30,y,x)
        editwin.attron(curses.color_pair(2))
        editwin.refresh()
        #editwin.encoding
        data = ""
        while True: #This while loop was made to create a custom str input that accepts icelandic chrs, the built in str input for curses only does ascci
            ch = editwin.getch()
            if ch== 10:
                break
            if (ch >=48 and ch <= 57) or (ch >=64 and ch <= 90) or (ch >=97 and ch <= 121)\
            or ch == 240 or ch == 230 or ch == 254 or ch == 46 or ch == 237 or ch == 205\
            or ch == 243 or ch == 211 or ch == 221 or ch == 253 or ch == 233 or ch == 201 \
            or ch == 250 or ch == 218 or ch == 225 or ch == 193 or ch == 32 or ch == ord(":"): #This defines all the chrs this custom input accepts
                data += chr(ch)
            elif ch == 8:
                data = data[:-1]
            elif data == 27:
                wrapper(main)
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
        self.print_menu(self.TUI_list, self.highlight_main_list[self.highlight_index], [0,0],[0,0])
        self.make_text_appear(21,68,"┌────────┐",12)
        self.make_text_appear(22,68,"|",12)
        self.make_text_appear(22,69," B",12,2)
        self.make_text_appear(22,71,"reyta |",12)
        self.make_text_appear(23,68,"└────────┘",12)
        if self.menu_select == 0:
            self.make_text_appear(5,4,self.header[self.menu_select][0] + ": " +item_list[self.menu_select][self.list_line_index][0],49)
            self.make_text_appear(9,4,self.header[self.menu_select][1] + ": " +item_list[self.menu_select][self.list_line_index][1],49)
            self.make_text_appear(12,4,self.header[self.menu_select][2] + ": " +item_list[self.menu_select][self.list_line_index][2],49)
            self.make_text_appear(16,4,self.header[self.menu_select][3] + ": " +item_list[self.menu_select][self.list_line_index][3],49)
            self.make_text_appear(5,53,self.header[self.menu_select][4] + ": " +item_list[self.menu_select][self.list_line_index][4],49)
            self.make_text_appear(9,53,"",49)
            self.make_text_appear(12,53,"",49)
            self.make_text_appear(16,53,"",49)
        if self.menu_select == 1:
            self.make_text_appear(5,4,self.header[self.menu_select][0] + ": " +item_list[self.menu_select][self.list_line_index][0],49)
            self.make_text_appear(9,4,self.header[self.menu_select][1] + ": " +item_list[self.menu_select][self.list_line_index][1],49)
            self.make_text_appear(12,4,self.header[self.menu_select][2] + ": " +item_list[self.menu_select][self.list_line_index][2],49)
            self.make_text_appear(16,4,self.header[self.menu_select][3] + ": " +item_list[self.menu_select][self.list_line_index][3],49)
            self.make_text_appear(5,53,self.header[self.menu_select][4] + ": " +item_list[self.menu_select][self.list_line_index][4],49)
            self.make_text_appear(9,53,self.header[self.menu_select][5] + ": " +item_list[self.menu_select][self.list_line_index][5],49)
            self.make_text_appear(12,53,self.header[self.menu_select][6] + ": " +item_list[self.menu_select][self.list_line_index][6],49)
            self.make_text_appear(16,53,self.header[self.menu_select][7] + ": " +item_list[self.menu_select][self.list_line_index][7],49)

        if self.menu_select == 2:
            self.make_text_appear(5,4,self.header[self.menu_select][0] + ": " +item_list[self.menu_select][self.list_line_index][0],49)
            self.make_text_appear(9,4,self.header[self.menu_select][1] + ": " +item_list[self.menu_select][self.list_line_index][1],49)
            self.make_text_appear(12,4,self.header[self.menu_select][2] + ": " +item_list[self.menu_select][self.list_line_index][2],49)
            self.make_text_appear(16,4,self.header[self.menu_select][3] + ": " +item_list[self.menu_select][self.list_line_index][3],49)
            self.make_text_appear(5,53,self.header[self.menu_select][4] + ": " +item_list[self.menu_select][self.list_line_index][4],49)
            self.make_text_appear(9,53,"",49)
            self.make_text_appear(12,53,"",49)
            self.make_text_appear(16,53,"",49)

        if self.menu_select == 3:
            self.make_text_appear(5,4,self.header[self.menu_select][0] + ": " +item_list[self.menu_select][self.list_line_index][0],49)
            self.make_text_appear(9,4,self.header[self.menu_select][1] + ": " +item_list[self.menu_select][self.list_line_index][1],49)
            self.make_text_appear(12,4,self.header[self.menu_select][2] + ": " +item_list[self.menu_select][self.list_line_index][2],49)
            self.make_text_appear(16,4,self.header[self.menu_select][3] + ": " +item_list[self.menu_select][self.list_line_index][3],49)
            self.make_text_appear(5,53,self.header[self.menu_select][4] + ": " +item_list[self.menu_select][self.list_line_index][4],49)
            self.make_text_appear(9,53,self.header[self.menu_select][5] + ": " +item_list[self.menu_select][self.list_line_index][5],49)
            self.make_text_appear(12,53,self.header[self.menu_select][6] + ": " +item_list[self.menu_select][self.list_line_index][6],49)
            self.make_text_appear(16,53,"",49)

        action = self.stdscr.getch()
        if action == ord("b"):
            self.change_user_menu()
    
    def change_user(self,index,y_position,extra_len):
        check = self.get_chr_from_user(y_position,2 + len(self.header[self.menu_select][index] + item_list[self.menu_select][self.list_line_index][index]) + extra_len)
        if check == 8:
            variable_x = self.make_user_input_window(y_position,6 + len(self.header[self.menu_select][index]) + extra_len)
        else:
            variable_x = item_list[self.menu_select][self.list_line_index][index]
        return variable_x

    def change_user_menu(self):
        if self.menu_select == 0:
            name = self.change_user(0,5,0)
            starf = self.change_user(1,9,0)
            rettindi = self.change_user(2,12,0)
            stada = self.change_user(3,16,0)
            afangastadur = self.change_user(4,5,49)

        if self.menu_select == 1:
            blah = self.change_user(0,5,0)
            blah = self.change_user(1,9,0)
            blah = self.change_user(2,12,0)
            blah = self.change_user(3,16,0)
            blah = self.change_user(4,5,49)
            blah = self.change_user(5,9,49)
            blah = self.change_user(6,12,49)
            blah = self.change_user(7,16,49)

        if self.menu_select == 2:
            blah = self.change_user(0,5,0)
            blah = self.change_user(1,9,0)
            blah = self.change_user(2,12,0)
            blah = self.change_user(3,16,0)
            blah = self.change_user(4,5,49)
            blah = self.change_user(5,9,49)
            blah = self.change_user(6,12,49)

        if self.menu_select == 3:
            blah = self.change_user(0,5,0)
            blah = self.change_user(1,9,0)
            blah = self.change_user(2,12,0)
            blah = self.change_user(3,16,0)
            blah = self.change_user(4,5,49)
            blah = self.change_user(5,9,49)
            blah = self.change_user(6,12,49)

    def get_chr_from_user(self,y,x):
        editwin = curses.newwin(1,1,y,4+x)

        editwin.attron(curses.color_pair(2))
        curses.curs_set(1)
        editwin.refresh()
        editwin.attroff(curses.color_pair(2))
        return editwin.getch()


    def main(self):
        # Clear screen
        self.stdscr.clear() 
        curses.init_color(1, 0, 0, 0)
        curses.can_change_color()
        curses.init_color(curses.COLOR_GREEN,1000,0,0)
        curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
        curses.init_pair(2,curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3,curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        
        # This raises ZeroDivisionError when i == 10.
        idx = 0
        idy = 0
        idz = 0
        list_den = [[1,1],[1,3],[1,5],[1,7]]
        list_den2 = [[3,1],[3,2],[3,3],[3,4],[3,5]]
        list_den3 = [[5,1],[6,1],[7,1],[8,1],[9,1],[10,1],[11,1],[12,1],[13,1],[14,1],[15,1],[16,1],[17,1],[18,1],[19,1],[20,1]]
        list_den4 = [[[22,4,"S"],[22,14,"N"],[22,24,"D"],[22,38,"F"]],[[22,4,"S"],[22,14,"N"],[22,24,"D"],[22,38,"V"]],[[22,4,"S"],[22,14,"N"]],[[22,4,"S"],[22,14,"N"],[22,24,"D"]]]
        list_den5 = ["x", " ", " "]
        while True:
            TUI_list = self.construct_TUI(list_den5)
            x = 4
            y = 10
            self.print_menu(TUI_list, list_den[idx], list_den3[idz],list_den4[idx])
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
                list_den5 = ["x", " ", " "]
                self.exeption = 0
                idx = 0
                self.highlight_index = 0
                idz = 0
            elif key == 50:
                self.menu_select = 1
                idx = 1
                self.highlight_index = 1
                idz = 0
            elif key == 51:
                self.menu_select = 2
                idx = 2
                self.highlight_index = 2
                idz = 0
            elif key == 52:
                self.menu_select = 3
                idx = 3
                self.highlight_index = 3
                idz = 0
                new_instance = LL_API()
                self.item_list1 = new_instance.get_all_airplanes()
                """for i in range(len(self.item_list1)):
                    for x in range(len(self.item_list1[i])):
                        self.stdscr.clear()
                        self.stdscr.attron(curses.color_pair(1))
                        self.stdscr.addstr(0,0,self.item_list1[i][x])
                        self.stdscr.attroff(curses.color_pair(1))
                        self.stdscr.refresh()
                        time.sleep(1) """
            elif key == curses.KEY_LEFT:
                if idy == 0:
                    idy = 4
                else:
                    idy -= 1
            elif key == curses.KEY_RIGHT:
                if idy == 4:
                    idy = 0
                else:
                    idy += 1
            elif key == curses.KEY_UP or key == 450:
                if idz == 0:
                    idz = 14
                    self.list_line_index = 14
                else:
                    idz -= 1
                    self.list_line_index -= 1
            elif key == curses.KEY_DOWN or key == 456:
                if idz == 14:
                    idz = 0
                    self.list_line_index = 0
                else:
                    idz += 1
                    self.list_line_index += 1
            elif key == 27:
                break
            elif key == ord("n"):
                self.new_registration = True
                self.new_reg_u_input = True
            elif key == ord("s"):
                self.check_specifcly = True
            if idx == 0:
                if key == 102:
                    buffer_str = list_den5.pop()
                    list_den5.insert(0,buffer_str)
                    if self.exeption != 2:
                        self.exeption += 1
                    else:
                        self.exeption = 0
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

#wrapper(start)