import random

def createRandomList(n, low, high):
    temp = []

    for i in range(n):
        temp.append(random.randrange(low, high))
    return temp

myRandomList = createRandomList(10, 1, 6)
print(myRandomList)