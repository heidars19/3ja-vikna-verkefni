import TUI.splash_screen
import time
time.sleep(1)
from TUI.Front_Layer_logic_TUI_Class5_0 import TUI
try:
    from curses import wrapper, color_pair
    import calendar
    def start(stdscr):
        new_tui = TUI(stdscr)
        
        new_tui.main()
    wrapper(start)

except ModuleNotFoundError:
    print("Ritaðu 'python pip3 install windows.curses' í útstöðina til að flytja niður viðaukan") #tekið úr tölvuorðasafninu frá 1999
