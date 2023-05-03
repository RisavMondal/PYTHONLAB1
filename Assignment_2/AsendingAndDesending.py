print("My Name is:- Risav MOndal Roll No:- 50")
x = int(input("Enter The Number of Array Elements:\t"))
array = []
for i in range(x):
    array.append(int(input(f"Enter the {i}th Number:\t")))


print(sorted(array))
print(sorted(array, reverse=True))