def min(list):
    
    if len(list) < 0:
        return False
    minVal = list[0]
    for i in list:
        if i < minVal:
            minVal = i
    return minVal


print(min([100, 45, 87, 24, 8, 88]))
