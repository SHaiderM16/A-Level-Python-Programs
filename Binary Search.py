# Binary Search Algorithm (Iterative)

def BinarySearch(SArray, UpperB, LowerB, SValue):
    isFound = False
    while LowerB <= UpperB and isFound == False:
        Mid = int((UpperB + LowerB) // 2)
        if SArray[Mid] == SValue:
            isFound = True
        elif SArray[Mid] < SValue:
            LowerB = Mid + 1
        elif SArray[Mid] > SValue:
            UpperB = Mid - 1
    if isFound:
        return Mid + 1
    else:
        return -1

# Binary Search Algorithm (Recursive)

def BinarySearchRecursive(SArray, UpperB, LowerB, SValue):
    Mid = int((UpperB + LowerB) // 2)
    if SArray[Mid] == SValue:
        return Mid + 1
    elif SArray[Mid] < SValue:
        return BinarySearchRecursive(SArray, UpperB, Mid + 1, SValue)
    elif SArray[Mid] > SValue:
        return BinarySearchRecursive(SArray, Mid - 1, LowerB, SValue)

MyList = []
for i in range(0, 10, 1):
    numbers = int(input("Enter the 10 numbers: "))
    MyList.append(numbers)

ValueToFind = int(input("Enter number to be found: "))

IterativeAnswer = BinarySearch(MyList, len(MyList) - 1, 0, ValueToFind)
RecursiveAnswer = BinarySearchRecursive(MyList, len(MyList) - 1, 0, ValueToFind)

if IterativeAnswer == -1:
    print(ValueToFind, "not found")
else:
    print(ValueToFind, "found at location", IterativeAnswer)

print("Using recursive algorithm,", ValueToFind, "found at location", RecursiveAnswer)
