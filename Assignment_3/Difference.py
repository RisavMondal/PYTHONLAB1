x = [1, 9, 3, 4, 5]
y = [1, 2, 3, 6, 7]

print("Difference is:\t")
for i in x:
    if i not in y:
        print(i, end="\t")