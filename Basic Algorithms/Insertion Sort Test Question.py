numbers = [8,4,9,2,6,3,7]
for currentnode in range (1,7):
    temp=numbers[currentnode]
    pointer= currentnode-1
    while numbers[pointer]>temp and pointer>-1:
        numbers[pointer+1] = numbers[pointer]
        pointer=pointer-1
    numbers[pointer+1]=temp
print(numbers)
