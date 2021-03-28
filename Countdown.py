def coundown(num):
    myList = []
    for i in range(num, -1, -1):
        myList.append(i)
    return myList


print(coundown(20))
