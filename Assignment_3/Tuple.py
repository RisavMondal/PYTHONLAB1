num = int(input("Enter How Many Numbers Are there:\t"))
x = []
for i in range(num):
    k = int(input(f"Enter the {i + 1}th Number:\t"))
    x.append((k, (k * k), (k * k * k)))

x = tuple(x)
print(x)