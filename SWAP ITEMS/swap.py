import random

def swap(index1 , index2, aList):
    aList[index1], aList[index2] = aList[index2], aList[index1]

myList = [1, 2, 3, 4]
swap(0, 2, myList)
print(myList)
