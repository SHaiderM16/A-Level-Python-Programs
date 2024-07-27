# Linked List Algorithms

class node:
    def __init__(self, DataP, NextNodeP):
        self.Data = DataP
        self.NextNode = NextNodeP

# DECLARE linkedList: ARRAY[0:9] OF node
linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]
StartPointer = 0
EmptyList = 5

def addNode(CurrentPointer):
    global linkedList
    global EmptyList
    Data = int(input("Enter the data to be added:"))
    if EmptyList < 0 or EmptyList > 9:
        return False
    else:
        FreeList = EmptyList
        EmptyList = linkedList[EmptyList].nextNode
        newNode = node(Data, -1)
        linkedList[FreeList] = newNode

        PreviousPointer = 0

        while CurrentPointer != -1:
            PreviousPointer = CurrentPointer
            CurrentPointer = linkedList[CurrentPointer].nextNode

        linkedList[PreviousPointer].nextNode = FreeList
        return True

def DeleteNode():
    global linkedList
    global StartPointer
    global EmptyList

    CurrentPointer = StartPointer

    Data = int(input("Enter the data to be deleted:"))

    PreviousPointer = 0
    while CurrentPointer != -1 and linkedList[CurrentPointer].Data != Data:
        PreviousPointer = CurrentPointer
        CurrentPointer = linkedList[CurrentPointer].NextNode

    if CurrentPointer == -1:
        return False
    else:
        if CurrentPointer == StartPointer:
            StartPointer = linkedList[StartPointer].NextNode
        else:
            linkedList[PreviousPointer].NextNode = linkedList[CurrentPointer].NextNode

        linkedList[CurrentPointer].Data = 0
        linkedList[CurrentPointer].Data = EmptyList
        EmptyList = CurrentPointer
        return True

def outputNodes():
    global linkedList
    CurrentPointer = StartPointer
    while CurrentPointer != -1:
        print(str(linkedList[CurrentPointer].Data))
        CurrentPointer = linkedList[CurrentPointer].NextNode

outputNodes()

def SearchItem(CurrentPointer, SearchVal):
    while CurrentPointer != -1:
        if linkedList[CurrentPointer].Data != SearchVal:
            CurrentPointer = linkedList[CurrentPointer].NextNode
        else:
            return CurrentPointer

        CurrentPointer = -1
        return CurrentPointer
