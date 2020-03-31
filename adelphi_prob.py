numOfList = int(input("Enter the number of lists you want to make: "))

myList = []

i = 1
count = 0

for list in range(numOfList):
    count = count + 3
    subList = []
    while(count >= i):
        subList.append(i)
        i = i + 1

    myList.append(subList)

print(myList)