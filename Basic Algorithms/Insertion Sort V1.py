MyList = []
print("Enter the 10 numbers")
for i in range(0, 10, 1):
    numbers = int(input("Enter here:"))
    MyList.append(numbers)

print("The unsorted list is:")
print(MyList)

# Insertion Sort Algorithm
def InsertionSort(SArray):
    for Pointer in range(1, len(SArray)):
        temp = SArray[Pointer]
        DecPointer = Pointer

        while DecPointer > 0 and SArray[DecPointer - 1] > temp:
            SArray[DecPointer] = SArray[DecPointer - 1]
            DecPointer = DecPointer - 1

        SArray[DecPointer] = temp

print("The sorted list is:")
InsertionSort(MyList)
print(MyList)
