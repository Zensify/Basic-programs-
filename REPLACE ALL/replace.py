def replaceAll(oldVal,newVal, aList):
    for i in range(len(aList)):
        if aList[i] == oldVal:
           aList[i] = newVal 

myList = ["a", "b", "c", "a", "b", "c", "a", "b", "c"]
replaceAll("a", "d", myList)
print(myList)