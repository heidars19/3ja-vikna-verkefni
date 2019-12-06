

def write_and_back(filename):
    filename2 = filename +".bak"

    with open(filename, 'r', encoding='utf-8') as file_original:
        with open(filename2, 'w+', encoding='utf-8') as file_bak:
            if isinstance(self._line_to_replace, int) : # If line_to_replace is a line number (int)
                for linenumber, line in enumerate(file_original):
                    if linenumber == self._line_to_replace :
                        file_bak.write(self._replace_with + '\n')
                    else :
                        file_bak.write(line)
            else :
                for line in file_original:
                    file_bak.write(line)

    with open(filename2, 'r', encoding='utf-8') as file_original:
        with open(filename, 'w+', encoding='utf-8') as file_bak:
            for line in file_original:
                file_bak.write(line)


write_and_back("Crew.csv")
