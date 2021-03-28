def reverse(list):
    for i in range(0, (len(list)-1)//2):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list


print(reverse([1, 2, 3]))
print(reverse([10, 20, 30, 40]))
print(reverse([100, 200, 300, 400]))
