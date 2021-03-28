# 13
b = 500
print(b)  # 500


def a():
    b = 300
    print(b)  # 500
    return b


print(b)  # 300
b = a()
print(b)  # 300
