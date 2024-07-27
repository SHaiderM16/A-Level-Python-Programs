# Circular Queue Algorithms

#DECLARE QueueArray: Array[0:9] OF STRING
QueueArray = []
for i in range(0, 10, 1):
    QueueArray.append("")
#DECLARE HeadPointer, TailPointer, NumberOfItems: INTEGER
HeadPointer = 0
TailPointer = 0
NumberOfItems = 0

# Enqueue Algorithm
def Enqueue(Value):
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberOfItems

    if NumberOfItems >= 10:
        return False

    QueueArray[TailPointer] = Value

    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer = TailPointer + 1
    NumberOfItems = NumberOfItems + 1
    return True

# Dequeue Algorithm
def Dequeue():
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberOfItems

    if NumberOfItems == 0:
        return False
    else:
        ReturnValue = QueueArray[HeadPointer]
        HeadPointer = HeadPointer + 1

        if HeadPointer > 9:
            HeadPointer = 0
        NumberOfItems = NumberOfItems - 1
        return ReturnValue
