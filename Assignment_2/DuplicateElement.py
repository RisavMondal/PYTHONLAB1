print("My Name is:- Risav MOndal Roll No:- 50")
x = int(input("Enter The Number of Array Elements:\t"))
array = []
for i in range(x):
    array.append(int(input(f"Enter the {i}th Number:\t")))


while len(array) != 0:
    x = array[0]
    array.remove(x)
    if x in array:
        print(f"{x} is having duplicates")
        while x in array:
            array.remove(x)
    else:
        print(f"{x} don't have duplicates.")