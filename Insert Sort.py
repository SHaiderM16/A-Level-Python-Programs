def InsertSort(SA, UB):
    for blackp in range(1, UB):
        for bluep in range(0, blackp):
            if SA[blackp]<SA[bluep]:
                temp=SA[blackp]
                for i in range(blackp, bluep, -1):
                    SA[i]=SA[i-1]
                SA[bluep]=temp
                break

SearchArray = [1,2,3,6,5,8,9,7]
x = len(SearchArray)
InsertSort(SearchArray, x)
print(SearchArray)
