import os


def readlines_reverse(filename, number_of_lines_to_read):
    with open(filename) as qfile:
        qfile.seek(0, os.SEEK_END)
        position = qfile.tell()
        line = ''
        while position >= 0:
            qfile.seek(position)

            for i in range(number_of_lines_to_read) :
                next_char = qfile.read(1)
                if next_char == "\n":
                    yield line[::-1]
                    line = ''
                else:
                    line += next_char
            position -= 1
        yield line[::-1]


if __name__ == '__main__':
    for qline in readlines_reverse("2001765459.csv",4):
        print(qline)