def bigger_size(list):

    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list


print(bigger_size([0, -2, -4, 6, 4, 2]))
