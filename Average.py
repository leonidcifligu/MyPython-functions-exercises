def avg(list):

    sum = 0
    avg = 0
    for i in list:
        sum += i
        avg = sum / len(list)
    return avg


print(avg([1, 2, 3, 4, 5]))
