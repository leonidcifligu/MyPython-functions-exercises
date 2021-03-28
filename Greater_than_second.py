def greater_than(list):
    if len(list) < 2:
        return False
    newList = []

    for value in list:
        if value > list[1]:
            newList.append(value)
    print(len(newList))
    return newList


print(greater_than([10, 20, 30, 40, 50, 60, 70, ]))
print(greater_than([20, 30, 40, 50, 60, 70, ]))
print(greater_than([1]))

