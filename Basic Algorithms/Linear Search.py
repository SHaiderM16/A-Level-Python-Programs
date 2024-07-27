# Linear Search Algorithm
def LinearSearch(SearchArray, Value):
    Found = False
    Index = 0
    MaxIndex = len(SearchArray)
    while Found == False and Index < MaxIndex:
        if MyList[Index] == ValueToFind:
            Found = True
        Index = Index + 1
    if Found == True:
        return Index
    else:
        return -1

MyList = []
for i in range(0, 10, 1):
    numbers = int(input("Enter the 10 numbers: "))
    MyList.append(numbers)

ValueToFind = int(input("Enter value to be found: "))

Answer = LinearSearch(MyList, ValueToFind)

if Answer == -1:
    print(ValueToFind, "is not found")
else:
    print(ValueToFind, "is found at location", Answer)
