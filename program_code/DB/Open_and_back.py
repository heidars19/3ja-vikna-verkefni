def write_and_back(file):
    filename = file
    filename2 = filename +".bak"

    with open(filename, 'r', encoding='utf-8') as readable:
        with open(filename2, 'w+', encoding='utf-8') as readable2:
            for line in readable:
                readable2.write(line)

    with open(filename2, 'r', encoding='utf-8') as readable:
        with open(filename, 'w+', encoding='utf-8') as readable2:
            for line in readable:
                readable2.write(line)

write_and_back("Crew.csv")