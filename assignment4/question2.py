def swap(x, y):
    x = x + y
    y = x - y
    x = x - y
    print(x, y)


x, y = 10, 20
print(x, y)
swap(x, y)