array = [1, 2, 8, 2, 3, 8, 2, 2, 1, 2, 2, 5, 1, 5,  3, 5]

done = []
for i in range(len(array)):
    count = 0
    if array[i] in done:
        continue
    for j in range(len(array)):
        if array[i] == array[j]:
            count += 1
    done.append(array[i])
    print(f"Frequency of {array[i]} is {count} times.")