MyList = []
for j in range(0, 10, 1):
    numbers = int(input("Enter the 10 numbers: "))
    MyList.append(numbers)

print("Unsorted Numbers:")
print(MyList)

# Bubble Sort Algorithm

def BubbleSort(SArray, UpperB):
    isSorted = True
    Temp = 0
    while isSorted == True:
        isSorted = False
        for i in range(1, UpperB, 1):
            if SArray[i] > SArray[i + 1]:
                Temp = SArray[i]
                SArray[i] = SArray[i + 1]
                SArray [i + 1] = Temp
                isSorted = True
        UpperB = UpperB - 1

BubbleSort(MyList, len(MyList) - 1)
print("Sorted Numbers:")
print(MyList)
