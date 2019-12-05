from TUI.Front_Layer_logic_TUI_Class2_0 import TUI
from curses import wrapper, color_pair

def start(stdscr):
    new_tui = TUI(stdscr)
    new_tui.main()

wrapper(start)