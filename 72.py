# Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами.
# Найти сумму элементов всей матрицы. Определить, какую долю в этой сумме составляет сумма элементов каждого столбца.
# Результат оформить в виде матрицы из N + 1 строк и M столбцов.

import random

N = 2
M = 3

def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 9))

    return col

def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix

def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1

        print()
        i += 1

def get_average(row):
    sum = 0
    for element in row:
        sum += element

    return sum/len(row)

def get_column(matrix, index):
    column = []
    i = 0
    while i < len(matrix):
        column.append(matrix[i][index])
        i += 1

    return column

A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)

sum = 0

i = 0
while i < len(A):
    j = 0

    while j < len(A[i]):
        sum += A[i][j]
        j += 1

    i += 1

i = 0
new_row = []
while i < len(A):
    j = 0

    while j < len(A[i]):
        if len(new_row) <= j:
            new_row.append(A[i][j])
        else:
            new_row[j] += A[i][j]
        j += 1

    i += 1

i = 0
while i < len(new_row):
    new_row[i] = new_row[i]/sum
    i += 1

A.append(new_row)

print("Сумма всех элементов:", sum)
print("Модифицированная матрица:")
print_matrix(A)
