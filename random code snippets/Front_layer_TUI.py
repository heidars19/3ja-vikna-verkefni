import curses
from curses import wrapper, color_pair



def print_menu(stdscr, TUI_list, list_den ,list_den3 ,idx ):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for y in range(len(TUI_list)):
        z = 0
        for x in range(len(TUI_list[y])):
            if y == list_den[0] and x == list_den[1]:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(y,z,TUI_list[y][x])
                stdscr.attroff(curses.color_pair(2))
            elif y == list_den3[0] and x == list_den3[1]:
                if list_den3[0] != 0:
                    stdscr.attron(curses.color_pair(2))
                    stdscr.addstr(y,z,TUI_list[y][x])
                    stdscr.attroff(curses.color_pair(2))
                else:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(y,z,TUI_list[y][x])
                    stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y,z,TUI_list[y][x])
                stdscr.attroff(curses.color_pair(1))
            z += len(TUI_list[y][x])
    if idx[0] != 0:
        for i in range(len(idx)):
            stdscr.delch(idx[i][0],idx[i][1])
            stdscr.insstr(idx[i][0],idx[i][1],idx[i][2],curses.color_pair(2))
    curses.curs_set(0)
    stdscr.refresh()
    