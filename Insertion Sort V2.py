# Insertion Sort Algo
def InsertSort(array):

    arraysize = len(array)

    for i in range(1, arraysize):
        insertvalue = array[i]
        pointer2 = i

        while pointer2 > 0 and array[pointer2 - 1] > insertvalue:
           array[pointer2] = array[pointer2 - 1]
           pointer2 = pointer2 - 1

        array[pointer2] = insertvalue

lst = []
for l in range(0, 10, 1):
    nums = int(input("Enter the numbers: "))
    lst.append(nums)

print(lst)

print(InsertSort(lst)
