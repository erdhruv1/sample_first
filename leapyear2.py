class LeapYear(object):

    #input funcion
    def input(self):
        self.year = int(input("Enter the year: "))
        print("the entered year is {0}".format(self.year))

    #condiditional satsfaction function
    def conditions(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    print("Year is a leap year")
                else:
                    print("year is not a leap year")
            else:
                print("It is a leap year")
        else:
            print("It is not a leap year")

#main function
def main():

    obj = LeapYear()
    obj.input()
    obj.conditions()

if __name__=="__main__":
    main()