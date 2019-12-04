import AirplaneFile


# class First:

#     def __init__(self):
#         self.second = Second()


#     def make_a_string(self):
#         return self.test


# class Second(First):

#     def __init__(self) :
#         self.test = "Þetta tókst"

#     def run_me(self) :
#         result = First.make_a_string(self)
#         print(result)


def main ():
    test = AirplaneFile()
    datalist = test.run_me()
    print(datalist)
    return

if __name__ == "__main__":
    main()