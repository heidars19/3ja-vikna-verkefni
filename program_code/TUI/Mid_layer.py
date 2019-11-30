import Front_layer
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


random_list1 = [[["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""],
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
                ],
                [["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð"],
                ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð"],
                ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð"],
                ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð"],
                ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð"],
                ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð"],
                ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"],
                ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð"]
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
                ["Berlín","Þýskaland","Berlin Airport","Baldur Magnússon","45443788643"]
                ],
                [["Batman","Boeing 747","400","Laus",""],
                ["Spiderman","Boeing 767","500","Lent ytra","New York"],
                ["Batman","Boeing 747","400","Laus",""],
                ["Spiderman","Boeing 767","500","Lent ytra","New York"],
                ["Batman","Boeing 747","400","Laus",""],
                ["Spiderman","Boeing 767","500","Lent ytra","New York"],
                ["Batman","Boeing 747","400","Laus",""],
                ["Spiderman","Boeing 767","500","Lent ytra","New York"],
                ["Batman","Boeing 747","400","Laus",""],
                ["Spiderman","Boeing 767","500","Lent ytra","New York"],
                ["Batman","Boeing 747","400","Laus",""],
                ["Spiderman","Boeing 767","500","Lent ytra","New York"],
                ["Batman","Boeing 747","400","Laus",""],
                ["Spiderman","Boeing 767","500","Lent ytra","New York"]
                ]
                ]


def starfsmannagluggi(item_list= []):
    item_list = [
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
    ["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""],
    ["Arnar Ívarsson","Flugþjónn","","Í ferð","New York"],
    ["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""]
    ]
    
    header = ["Nafn","Starf","Réttindi","Staða","Áfangastaður"]
    footer = ["{:^{lengd:}}".format("Skoða",lengd = 7),\
        "{:^{lengd:}}".format("Nýskrá",lengd = 7),\
        "{:^{lengd:}}".format("Dagur",lengd = 7),\
        "{:^{lengd:}}".format("Flokka",lengd = 7)]
    
    new_list = []
    for i in range(len(item_list)):
        new_string = ""
        for x in range(len(item_list[i])):
            new_string += "{:^{lengd:}}".format(item_list[i][x],lengd = header_lengd)
        new_list.append(new_string)
    
    header_list = []
    for i in range(len(header)):
        new_string = "{:^{lengd:}}".format(header[i],lengd = header_lengd)
        header_list.append(new_string)
    #z = "{:^{lengd:}}".format("",lengd = 7)
    #x = "{:^{lengd:}}".format("",lengd = header_lengd)
    
    


    TUI_list = (
    (("╔════════════════════╦════════════════════╦════════════════════╦════════════════════╦════════════════════╗")),
    (("║"),(h_starf) ,    ("║") ,(h_vinnufe) , ("║") ,(h_afangas) , ("║"), (h_flugvel) , ("║"),(get_date),    ("║")),
    (("╠════════════════════╩════════════════════╩════════════════════╩════════════════════╝                    ║")),
    (("║  "),(header_list[0]),(header_list[1]),(header_list[2]),(header_list[3]),(header_list[4]),          ("  ║")),
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
    (("║ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐                                                                ║")),
    (("║ │"),(footer[0]),("| |"),(footer[1]),("| |"),(footer[2]),("| |"),(footer[3]),("|                                                                ║")),
    (("║ └───────┘ └───────┘ └───────┘ └───────┘                                                                ║")),
    (("╚════════════════════════════════════════════════════════════════════════════════════════════════════════╝")))
    

    return TUI_list


def vinnuferðagluggi(item_list = []):
    item_list =[
    ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"],
    ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð"],
    ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"],
    ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð"],
    ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"],
    ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð"],
    ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"],
    ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð"],
    ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"],
    ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð"],
    ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"],
    ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð"],
    ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"],
    ["15/12/19","13:00","Kúlusúkk","Boeing 767","Mönnuð"],
    ["14/12/19","14:30","Svalbarði","Boeing 787","Ómönnuð"]
    ]
    
    header = ["Nafn","Starf","Réttindi","Staða","Áfangastaður"]
    
    new_list = []
    for i in range(len(item_list)):
        new_string = ""
        for x in range(len(item_list[i])):
            new_string += "{:^{lengd:}}".format(item_list[i][x],lengd = header_lengd)
        new_list.append(new_string)
    
    header_list = []
    for i in range(len(header)):
        new_string = "{:^{lengd:}}".format(header[i],lengd = header_lengd)
        header_list.append(new_string)
    
    z = "{:^{lengd:}}".format("",lengd = 7)
    x = "{:^{lengd:}}".format("",lengd = header_lengd)

    TUI_list = (
    (("╔════════════════════╦════════════════════╦════════════════════╦════════════════════╦════════════════════╗")),
    (("║"),(h_starf) ,    ("║") ,(h_vinnufe) , ("║") ,(h_afangas) , ("║"), (h_flugvel) , ("║       Vika 32      ║")),
    (("╠════════════════════╩════════════════════╩════════════════════╩════════════════════╝                    ║")),
    (("║  "),(header_list[0]),(header_list[1]),(header_list[2]),(header_list[3]),(header_list[4]),          ("  ║")),
    (("║ ┌───────────────────────────────────────────────────────────────────────────────────────────────────┐  ║")),
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
    (("║ └───────────────────────────────────────────────────────────────────────────────────────────────────┘  ║")),
    (("║  "),(z),(z),(z),(z),(x),                                                                           ("  ║")),
    (("║  "),(z),(z),(z),(z),(x),                                                                           ("  ║")),
    (("║  "),(z),(z),(z),(z),(x),                                                                           ("  ║")),
    (("╚════════════════════════════════════════════════════════════════════════════════════════════════════════╝")))
    return TUI_list


def menu_constants(idx,random_list = []):
    if idx == 0:
        TUI_list = starfsmannagluggi()
    if idx == 1:
        TUI_list = vinnuferðagluggi()
    
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
    while True:
        TUI_list = menu_constants(idx)
        curses.curs_set(1)
        Front_layer.create_menu(stdscr, TUI_list, list_den[idx], list_den2[idy], list_den3[idz])
        key = stdscr.getch()
        if key == 49:
            idx = 0
        elif key == 50:
            idx = 1
        elif key == 51:
            idx = 2
        elif key == 52:
            idx = 3
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
        """stdscr.clear()
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(0,0,str(key))
        stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        time.sleep(0.5)"""
    curses.curs_set(1)

#curses.cbreak
#curses.nocbreak
wrapper(main)
