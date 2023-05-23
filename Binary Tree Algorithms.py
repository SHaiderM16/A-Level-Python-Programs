# Binary Tree Algorithms

ArrayNodes = [[0] * 3 for i in range(0, 20, 1)]
RootPointer = -1
FreeNode = 0

def AddNode():
    global ArrayNodes
    global RootPointer
    global FreeNode

    NodeData = int(input("Enter the data:"))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1

        if RootPointer == -1:
            RootPointer = 0
        else:
            isInserted = False
            CurrentPointer = RootPointer
            while isInserted == False:
                if NodeData < ArrayNodes[CurrentPointer][1]:
                    if ArrayNodes[CurrentPointer][0] == -1:
                        ArrayNodes[CurrentPointer][0] = FreeNode
                        isInserted = True
                    else:
                        CurrentPointer = ArrayNodes[CurrentPointer][0]
                else:
                    if ArrayNodes[CurrentPointer][2] == -1:
                        ArrayNodes[CurrentPointer][2] = FreeNode
                        isInserted = True
                    else:
                        CurrentPointer = ArrayNodes[CurrentPointer][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")

def FindNode(SVal):
    CurrentPointer = RootPointer

    while CurrentPointer != -1 and ArrayNodes[CurrentPointer][1] != SVal:
        if SVal < ArrayNodes[CurrentPointer][1]:
            CurrentPointer = ArrayNodes[CurrentPointer][0]
        else:
            CurrentPointer = ArrayNodes[CurrentPointer][2]

    print(CurrentPointer)

# Traversals; InOrder = L + Root + R; PreOrder = Root + L + R, PostOrder = L + R + Root
def InOrderT(BTArray, Root):
    if BTArray[Root][0] != -1:
        InOrderT(BTArray, BTArray[Root][0])
    print(str(BTArray[Root][1]))
    if BTArray[Root][2] != -1:
        InOrderT(BTArray, BTArray[Root][2])
