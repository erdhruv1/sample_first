import random

lower = 0
upper = 10

def give_me_even_value():
    while(1):
        value = random.randint(lower, upper)

        if value % 2 == 0:
            return value
        else:
            continue

def give_me_odd_value():
    while (1):
        value = random.randint(lower, upper)

        if value % 2 != 0:
            return value
        else:
            continue

def main():
    my_list = []
    for i in range(4):

        even_value = give_me_even_value() #100% we gonna get even value
        odd_value  = give_me_odd_value() # 100% we gonna get odd value

        if i % 2 == 0:
            my_list.append(even_value)
        else:
            my_list.append(odd_value)

    print(my_list)

if __name__ == '__main__':
    main()