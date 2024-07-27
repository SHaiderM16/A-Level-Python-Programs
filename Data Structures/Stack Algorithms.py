# Stack Algorithms

global StackData
global StackPointer
StackData = [0] * 10
StackPointer = 0

def PrintStack():
    global StackData
    global StackPointer
    print(StackPointer)
    for j in range(0, 10):
        print(StackData[j])

# Push Algorithm
def Push(Value):
    global StackData
    global StackPointer
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = Value
        StackPointer = StackPointer + 1
        return True

for k in range(0, 11, 1):
    Number = int(input("Enter the number:"))
    if Push(Number):
        print("Number successfully added")
    else:
        print("The stack is full")

PrintStack()

# Pop Algorithm
def Pop():
    global StackData
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        StackPointer = StackPointer - 1
        TopElement = StackData[StackPointer]
        return TopElement
