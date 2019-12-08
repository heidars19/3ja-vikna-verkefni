
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


def construct_footer(x_list):
    top_box1 = box_frame(MENU_BOX_1_LENGTH)
    top_box2 = box_frame(MENU_BOX_2_LENGTH)
    top_box3 = box_frame(MENU_BOX_3_LENGTH)
    top_box4 = box_frame(MENU_BOX_4_LENGTH)
    top_box5 = box_frame(MENU_BOX_5_LENGTH)
    bot_box1 = box_frame(MENU_BOX_1_LENGTH,"not top")
    bot_box2 = box_frame(MENU_BOX_2_LENGTH,"not top")
    bot_box3 = box_frame(MENU_BOX_3_LENGTH,"not top")
    bot_box4 = box_frame(MENU_BOX_4_LENGTH,"not top")
    bot_box5 = box_frame(MENU_BOX_5_LENGTH,"not top")
    check_box_left = " ("
    check_box_right = ")"
    check_box_x = x_list
    one_space_string = "  "
    empty_string1 = "     "
    empty_string2 = "         "
    Flokka_listi = [[
    " {:<{MENU_OPTION_LENGTH:}}".format(MENU_OPTION_1),
    " {:<{MENU_OPTION_LENGTH:}}".format(MENU_OPTION_2),
    " {:<{MENU_OPTION_LENGTH:}}".format(MENU_OPTION_3),
    ],
    [
    " {:<{lengd:}}".format("",lengd = MENU_OPTION_LENGTH + 3),
    ]
    ]
    footer = (
    (
    (top_box1,top_box2,top_box3,top_box4, check_box_left + check_box_x[0] + check_box_right + Flokka_listi[0][0]),
    (MENU_BUTTON_1,MENU_BUTTON_2,MENU_BUTTON_3,MENU_BUTTON_4, check_box_left + check_box_x[1] + check_box_right + Flokka_listi[0][1]
    ),
    (bot_box1,bot_box2,bot_box3,bot_box4,check_box_left + check_box_x[2] + check_box_right + Flokka_listi[0][2])
    ),
    (
    (top_box1,top_box2,top_box3,top_box5, one_space_string + Flokka_listi[1][0]),
    (MENU_BUTTON_1,MENU_BUTTON_2,MENU_BUTTON_3,MENU_BUTTON_5,one_space_string + Flokka_listi[1][0]
    ),
    (bot_box1,bot_box2,bot_box3,bot_box5,one_space_string + Flokka_listi[1][0])
    ),
    (
    (top_box1,top_box2,empty_string2,empty_string2, empty_string1 + Flokka_listi[1][0]),
    (MENU_BUTTON_1,MENU_BUTTON_2,\
    "{:^{lengd:}}".format("",lengd = 9),\
    "{:^{lengd:}}".format("",lengd = 9) ,
    empty_string1 + Flokka_listi[1][0]
    ),
    (bot_box1,bot_box2,empty_string2,empty_string2,empty_string1 + Flokka_listi[1][0])
    ),
    (
    (top_box1,top_box2,top_box3,empty_string2, one_space_string + Flokka_listi[1][0]),
    (MENU_BUTTON_1,MENU_BUTTON_2,MENU_BUTTON_3,\
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

print(construct_footer(["x","",""]))