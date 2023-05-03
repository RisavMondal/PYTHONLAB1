def display(matrix):
    row = len(matrix)
    col = len(matrix[0])

    for r in range(row):
        for c in range(col):
            print(matrix[r][c], end='\t')
        print()


def createDummy(row, col):
    x = []
    for r in range(row):
        t = []
        for c in range(col):
            t.append(0)
        x.append(t)
    return x


def takeInput():
    row = int(input("How many rows are there in matrix\t"))
    col = int(input("Number of columns in matrix:\t"))
    matrix = []
    for r in range(row):
        temp = []
        for c in range(col):
            temp.append(int(input(f"Element ({r}, {c}) is:\t")))
        matrix.append(temp)
    return row, col, matrix


def addition():
    row1, col1, matrix1 = takeInput()
    row2, col2, matrix2 = takeInput()
    sum_m = []
    if row1 == row2 and col1 == col2:
        for r in range(row1):
            temp = []
            for c in range(col1):
                temp.append(matrix1[r][c] + matrix2[r][c])
            sum_m.append(temp)
    return sum_m


def subtraction():
    row1, col1, matrix1 = takeInput()
    row2, col2, matrix2 = takeInput()
    sub_m = []
    if row1 == row2 and col1 == col2:
        for r in range(row1):
            temp = []
            for c in range(col1):
                temp.append(matrix1[r][c] - matrix2[r][c])
            sub_m.append(temp)
    return sub_m


def multiplication():
    row1, col1, matrix1 = takeInput()
    row2, col2, matrix2 = takeInput()
    mul_m = createDummy(row1, col2)

    if col1 == row2:
        for r1 in range(row1):
            for c2 in range(col2):
                for r2 in range(row2):
                    mul_m[r1][c2] += matrix1[r1][r2] * matrix2[r2][c2]
    return mul_m


def transpose():
    row, col, matrix = takeInput()
    tran_m = createDummy(col, row)

    for r in range(row):
        for c in range(col):
            tran_m[c][r] = matrix[r][c]
    return tran_m

print("My name is :Risav Mondal Roll is:50")
display(addition())
display(subtraction())
display(multiplication())
display(transpose())