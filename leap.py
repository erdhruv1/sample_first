print("Enter the year:")
year = int(input())

if year%4 == 0 and year%100 != 0:
    print("It is a leap year")

elif year%100 == 0:
    print("It is not a leap year")

elif year%400 == 0:
    print("It is a leap year")

else:
    print("It is not a leap year")