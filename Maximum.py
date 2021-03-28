def maximum(list):

    maxVal = list[0]
    for num in list:
        if maxVal < num:
            maxVal = num
    return maxVal


print(maximum([100, 45, 87, 24, 8, 88]))
