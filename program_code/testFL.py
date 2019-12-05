from TUI.Front_Layer_logic_TUI_Class2_0 import TUI
from curses import wrapper, color_pair
import calendar
def start(stdscr):
    new_tui = TUI(stdscr)
    new_tui.main()

#wrapper(start)
cal = calendar.Calendar()
month = cal.monthdatescalendar(year = 2019,month = 12)
for i in range(len(month)):
    for x in range(len(month)):
        print(month[i][x])