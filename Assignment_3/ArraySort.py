import random


def arraySort(array: list):
    return sorted(array)


num = 10
x = []
for i in range(num):
    x.append(random.randint(10, 50))


print("Sorted Array is:\t", arraySort(x))
