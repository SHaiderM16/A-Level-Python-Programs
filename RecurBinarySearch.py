def RecursiveBinarySearch(SearchArray, UpperBound, LowerBound, Val):
    if LowerBound > UpperBound:
        return -1
    else:
        MID = int((LowerBound+UpperBound)//2)
        if SearchArray[MID] == Val:
            return MID
        elif SearchArray[MID] > Val:
            return RecursiveBinarySearch(SearchArray, MID-1, LowerBound, Val)
        elif SearchArray[MID] < Val:
            return RecursiveBinarySearch(SearchArray, UpperBound, MID + 1, Val)
SearchArray=["a","b","c","d"]
LowerBound=0
UpperBound=3
Val=input("Enter the value to be found: ")
Result=RecursiveBinarySearch(SearchArray, UpperBound, 0, Val)
if Result==-1:
    print(Val, "not found.")
else:
    print(Val, "found at index", Result)
