def count_positives(list):
   
    count = 0
    for i in (list):
        if i > 0:
            count += 1
    list[len(list)-1] = count
    return list


print([-6, -4, -2, 0, 2, 4, 6])
print(count_positives([-6, -4, -2, 0, 2, 4, 6]))
