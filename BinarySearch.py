SearchArray = [1,2,3,4,5,6,7,8,9]
def BinarySearch(Val):
    IsFound = False
    LowerBound = 0
    UpperBound = 8
    while UpperBound >= LowerBound and IsFound == False:
        Middle = (LowerBound + UpperBound) // 2
        if SearchArray[Middle] == Val:
            IsFound = True
            return Middle
        elif Val > SearchArray[Middle]:
            LowerBound = Middle + 1
        elif Val < SearchArray[Middle]:
            UpperBound = Middle - 1
    return -1
x = int(input("Enter the number to search: "))
print (x, "found at location", BinarySearch(x))