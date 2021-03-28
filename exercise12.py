# 12
b = 500
print(b)  # 500


def a():
    b = 300
    print(b)
    return b  # 500


print(b)  # 300
a()
print(b)  # 500
