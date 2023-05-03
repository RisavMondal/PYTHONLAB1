
print("My Name is:- Risav Mondal Roll No:- 50")
x = int(input("Enter The Number of Array Elements:\t"))
array = []
for i in range(x):
    array.append(int(input(f"Enter the {i}th Number:\t")))

for i in range(len(array)):
    count = 0
    for j in range(len(array)):
        if array[i] == array[j]:
            count += 1
    print(f"Frequency of {array[i]} is {count} times.")