def countItems(aList, anItem):
    counter = 0

    for i in range(len(aList)):
        #print(i)
        if aList[i] == anItem:
            counter += 1
    return counter

print(countItems([1, 3, 7, 7, 5, 7, 7], 7))
print(countItems([1, 3, 7, 7, 5, 7, 7], 5))