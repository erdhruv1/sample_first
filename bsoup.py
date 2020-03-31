class ABCD:

    #Constructor
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def display(self):
        print("Hello Prabal")

    def sum(self):
        num3 = self.number1 + self.number2
        return num3

def main():
    #Instantiation of a class
    obj = ABCD()    # __init__ method will get invoked automatically

    obj.display()
    result = obj.sum()
    print("The sum of 2 and 3 is : {0}".format(result))

if __name__ == "__main__":
    main()