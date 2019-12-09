

new_list = [["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""],
                ["Arnar Ívarsson","Flugþjónn","","Í ferð","New York"],
                ["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""],
                ["Arnar Ívarsson","Flugþjónn","","Í ferð","New York"],
                ["Arnar Ívarsson","Flugþjónn","","Í ferð","New York"],
                ["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""],
                ["Arnar Ívarsson","Flugþjónn","","Í ferð","New York"],
                ["Sigurgeir Helgason","Flugmaður","Boeing 747","Laus",""]
                ]


def body_template_func(new_list) :
    template_list = []
    template_list.append(("║ ┌────────────────────────────────────────────────────────────────────────────────────────────────────┐ ║"))
    for i in range(15):
        temp_tuple = (("║ │"), (new_list[i]),("│ ║") )
        template_list.append( temp_tuple )
    template_list.append(("║ └────────────────────────────────────────────────────────────────────────────────────────────────────┘ ║"))
    return tuple(template_list)
    
    
            

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



result = body_template_func(new_list)

#print(result)
# for line in result:
#     print(line)
    
    
print(body_template)