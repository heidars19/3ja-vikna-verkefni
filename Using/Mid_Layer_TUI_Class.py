import User_interface
import Front_layer_TUI
import curses
import time
import datetime
from curses import wrapper, color_pair
header_lengd = 20



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
class TUI_Builder():
    def __init__(self):
        self.menu_select = 0
        self.exeption = 0
    def construct_TUI(self,x_list):
        main_menu_temp = self.construct_main_menu()
        header_temp = self.construct_header()
        body_temp = self.construct_body()
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
        date = str(datetime.date.today())
        get_date = "{:^{lengd:}}".format(date,lengd = header_lengd)
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
        header = (\
        ("Nafn","Starf","Réttindi","Staða","Áfangastaður"),\
        ("Dagsetning","Brottför","Áfangastaður","Flugvél","Mönnun","Flugnr.","Sæti","Staða"),\
        ("Nafn","Land","FlugVöllur","Tengiliður","Sími"),\
        ("Nafn","Tegund","Sæti","Staða","Áfangastaður","Flugnr.","Aflögufær"))
        header_string = ""
        for i in range(len(header[self.menu_select])):
            header_string += "{:^{lengd:}}".format(header[self.menu_select][i],lengd = int(100/(len(header[self.menu_select]))))
        for i in range(100-len(header_string)):
            header_string += " "
        header_template = (
        (("║  "),(header_string),("  ║")),
        )
        return header_template
    
    def construct_body(self):
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
        " {:<{lengd:}}".format("",lengd = 12),
        ]
        ]
        footer = (
        (
        (top_box,top_box3,top_box,top_box3, check_box_left + check_box_x[0] + check_box_right + Flokka_listi[0][0]),
        (
        "{:^{lengd:}}".format("| Skoða |",lengd = 9),\
        "{:^{lengd:}}".format("| Nýskrá |",lengd = 10),\
        "{:^{lengd:}}".format("| Dagur |",lengd = 9),\
        "{:^{lengd:}}".format("| Flokka |",lengd = 10),
        check_box_left + check_box_x[1] + check_box_right + Flokka_listi[0][1]
        ),
        (bot_box,bot_box3,bot_box,bot_box3,check_box_left + check_box_x[2] + check_box_right + Flokka_listi[0][2])
        ),
        (
        (top_box,top_box3,top_box,top_box, empty_string1 + Flokka_listi[1][0]),
        (
        "{:^{lengd:}}".format("| Skoða |",lengd = 9),\
        "{:^{lengd:}}".format("| Nýskrá |",lengd = 10),\
        "{:^{lengd:}}".format("| Dagur |",lengd = 9) ,\
        "{:^{lengd:}}".format("| Vika  |",lengd = 9),
        empty_string1 + Flokka_listi[1][0]
        ),
        (bot_box,bot_box3,bot_box,bot_box,empty_string1 + Flokka_listi[1][0])
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
        (("║ "),(footer[self.menu_select][0][0]),(" "),(footer[self.menu_select][0][1]),(" "),(footer[self.menu_select][0][2]),(" "),(footer[self.menu_select][0][3]),(footer[self.menu_select][0][4]),("                                             ║")),
        (("║ "),(footer[self.menu_select][1][0]),(" "),(footer[self.menu_select][1][1]),(" "),(footer[self.menu_select][1][2]),(" "),(footer[self.menu_select][1][3]),(footer[self.menu_select][1][4]),("                                             ║")),
        (("║ "),(footer[self.menu_select][2][0]),(" "),(footer[self.menu_select][2][1]),(" "),(footer[self.menu_select][2][2]),(" "),(footer[self.menu_select][2][3]),(footer[self.menu_select][2][4]),("                                             ║")),
        (("╚════════════════════════════════════════════════════════════════════════════════════════════════════════╝")))
        return footer_template




def main(stdscr):
    # Clear screen
    stdscr.clear() 
    curses.init_pair(1,curses.can_change_color(), curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_YELLOW, curses.COLOR_BLACK)
    
    # This raises ZeroDivisionError when i == 10.
    idx = 0
    idy = 0
    idz = 0
    list_den = [[1,1],[1,3],[1,5],[1,7]]
    list_den2 = [[3,1],[3,2],[3,3],[3,4],[3,5]]
    list_den3 = [[5,1],[6,1],[7,1],[8,1],[9,1],[10,1],[11,1],[12,1],[13,1],[14,1],[15,1],[16,1],[17,1],[18,1],[19,1],[20,1]]
    list_den4 = [[[22,4,"S"],[22,14,"N"],[22,25,"D"],[22,35,"F"]],[[22,4,"S"],[22,14,"N"],[22,25,"D"],[22,35,"V"]],[[22,4,"S"],[22,14,"N"]],[[22,4,"S"],[22,14,"N"],[22,24,"D"]]]
    list_den5 = ["x", " ", " "]
    TUI_instance = TUI_Builder()
    while True:
        TUI_list = TUI_instance.construct_TUI(list_den5)
        x = 4
        y = 10
        curses.curs_set(0)
        curses.noecho()
        Front_layer_TUI.create_menu(stdscr, TUI_list, list_den[idx], list_den2[idy], list_den3[idz],list_den4[idx])
        #string_input = stdscr.getstr(21, 70)
        key = stdscr.getch()
        if key == 49:
            TUI_instance.menu_select = 0
            list_den5 = ["x", " ", " "]
            TUI_instance.exeption = 0
            idx = 0
            idz = 0
        elif key == 50:
            TUI_instance.menu_select = 1
            idx = 1
            idz = 0
        elif key == 51:
            TUI_instance.menu_select = 2
            idx = 2
            idz = 0
        elif key == 52:
            TUI_instance.menu_select = 3
            idx = 3
            idz = 0
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
        elif key == curses.KEY_UP:
            if idz == 0:
                idz = 14
            else:
                idz -= 1
        elif key == curses.KEY_DOWN:
            if idz == 14:
                idz = 0
            else:
                idz += 1
        elif key == 27:
            break
        if idx == 0:
            if key == 102:
                buffer_str = list_den5.pop()
                list_den5.insert(0,buffer_str)
                if TUI_instance.exeption != 2:
                    TUI_instance.exeption += 1
                else:
                    TUI_instance.exeption = 0
        
        """stdscr.clear()
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(0,0,str(TUI_instance.menu_select))
        stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        time.sleep(1)"""
    curses.curs_set(0)

#curses.cbreak
#curses.nocbreak
time.sleep(1)
wrapper(main)

"""tui = TUI_Builder()
tui.menu_select = 1
tui.construct_TUI(["x","",""])"""