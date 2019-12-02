import Front_layer_TUI
import curses
import time
import datetime
from curses import wrapper, color_pair

menu = ("1.Starfsmenn", "2.Vinnuferðir", "3.Áfangastaðir", "4.Flugvélar")
header_lengd = 20
h_starf = "{:^{lengd:}}".format(menu[0],lengd = header_lengd)
h_vinnufe = "{:^{lengd:}}".format(menu[1],lengd = header_lengd)
h_afangas = "{:^{lengd:}}".format(menu[2],lengd = header_lengd)
h_flugvel = "{:^{lengd:}}".format(menu[3],lengd = header_lengd)
date = str(datetime.date.today())
get_date = "{:^{lengd:}}".format(date,lengd = header_lengd)


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
def starfsmannagluggi(idx,x_list):
    header = (\
        ("Nafn","Starf","Réttindi","Staða","Áfangastaður"),\
        ("Dagsetning","Brottför","Áfangastaður","Flugvél","Mönnun","Flugnr.","Sæti","Staða"),\
        ("Nafn","Land","FlugVöllur","Tengiliður","Sími"),\
        ("Nafn","Tegund","Sæti","Staða","Áfangastaður","Flugnr.","Aflögufær"))
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
    new_list = []
    for i in range(len(item_list[idx])):
        new_string = ""
        for x in range(len(item_list[idx][i])):
            new_string += "{:^{lengd:}}".format(item_list[idx][i][x],lengd = int(100/(len(item_list[idx][i]))))
        new_list.append(new_string)
    for i in range(len(new_list)):
        for x in range(100-len(new_list[i])):
            new_list[i] += " "
    header_string = ""
    for i in range(len(header[idx])):
        header_string += "{:^{lengd:}}".format(header[idx][i],lengd = int(100/(len(header[idx]))))
    for i in range(100-len(header_string)):
        header_string += " "
    TUI_list = (
    (("╔════════════════════╦════════════════════╦════════════════════╦════════════════════╦════════════════════╗")),
    (("║"),(h_starf) ,    ("║") ,(h_vinnufe) , ("║") ,(h_afangas) , ("║"), (h_flugvel) , ("║"),(get_date),    ("║")),
    (("╠════════════════════╩════════════════════╩════════════════════╩════════════════════╝                    ║")),
    (("║  "),(header_string)                                                                     ,          ("  ║")),
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
    (("║ └────────────────────────────────────────────────────────────────────────────────────────────────────┘ ║")),
    (("║ "),(footer[idx][0][0]),(" "),(footer[idx][0][1]),(" "),(footer[idx][0][2]),(" "),(footer[idx][0][3]),(footer[idx][0][4]),("                                             ║")),
    (("║ "),(footer[idx][1][0]),(" "),(footer[idx][1][1]),(" "),(footer[idx][1][2]),(" "),(footer[idx][1][3]),(footer[idx][1][4]),("                                             ║")),
    (("║ "),(footer[idx][2][0]),(" "),(footer[idx][2][1]),(" "),(footer[idx][2][2]),(" "),(footer[idx][2][3]),(footer[idx][2][4]),("                                             ║")),
    (("╚════════════════════════════════════════════════════════════════════════════════════════════════════════╝")))
    
    
    return TUI_list

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
    while True:
        TUI_list = starfsmannagluggi(idx, list_den5)
        x = 4
        y = 10
        curses.curs_set(0)
        curses.noecho()
        Front_layer_TUI.create_menu(stdscr, TUI_list, list_den[idx], list_den2[idy], list_den3[idz],list_den4[idx])
        #stdscr.getstr(10, 10) Sækir streng frá notenda á x,y
        key = stdscr.getch()
        if key == 49:
            idx = 0
            idz = 0
        elif key == 50:
            idx = 1
            idz = 0
        elif key == 51:
            idx = 2
            idz = 0
        elif key == 52:
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
        
        """stdscr.clear()
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(0,0,str(key))
        stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        time.sleep(1)"""
    curses.curs_set(0)

#curses.cbreak
#curses.nocbreak
wrapper(main)
