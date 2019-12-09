"""import TUI.User_interface
import time
time.sleep(1)"""
from TUI.Front_Layer_logic_TUI_Class3_0 import TUI
try:
    from curses import wrapper, color_pair
except:
    print("type 'pip3 install windows.curses' in terminal to get the needed extesion")
    import calendar
    def start(stdscr):
        new_tui = TUI(stdscr)
        new_tui.main()

    wrapper(start)


