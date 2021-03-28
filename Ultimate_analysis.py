def ultimate_analysis(list):
    myList = {'sum': 0, 'avg': 0,'min': list[0], 'max': list[0], 'length': len(list)}
    for i in list:
        if myList['min'] < i:
            myList['min'] = i
        if myList['max'] > i:
            myList['max'] = i
            myList['sum'] += i
            myList['avg'] = myList['sum']/len(list)
    return myList


print(ultimate_analysis([1, 2, 3, 4, 5, 6]))
print(ultimate_analysis([3, 5]))
print(ultimate_analysis([1988, 24, 8]))
