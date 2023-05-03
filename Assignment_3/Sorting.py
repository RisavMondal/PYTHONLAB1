num = int(input("Enter The Number of Elements:\t"))
x = []
for i in range(num):
    x.append(input(f"Enter The {i + 1}th Element:\t"))

print(sorted(x))
print(sorted(x, reverse=True))