import numpy as np


def take_matrix():
    matrix_size = list(map(int, input("Enter the size of matrix:").split()))
    matrix = list()
    print("Enter matrix:")
    for x in range(matrix_size[0]):
        matrix.append(list(map(float, input().split())))
    return matrix, matrix_size


def print_matrix(mat):
    print("The result is:")
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if type(mat[i][j]) == float:
                if mat[i][j] == int(mat[i][j]):
                    print(int(mat[i][j]), end=" ")
                else:
                    # mat[i][j] = int(mat[i][j] * 100) / 100
                    mat[i][j] = round(mat[i][j], 3)
                    print(mat[i][j], end=" ")
        print()


def side_transpose(mat):
    result = [[0 for x in range(len(mat))] for y in range(len(mat[0]))]

    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            result[i][j] = mat[len(mat) - 1 - j][len(mat[0]) - 1 - i]
    return result


def vertical_transpose(mat):
    result = [[0 for x in range(len(mat))] for y in range(len(mat[0]))]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            result[i][j] = mat[i][len(result) - 1 - j]
    return result


def horizontal_transpose(mat):
    result = [[0 for x in range(len(mat))] for y in range(len(mat[0]))]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            result[len(result) - 1 - i][j] = mat[i][j]
    return result


def main_transpose(mat):
    result = [[0 for x in range(len(mat))] for y in range(len(mat[0]))]

    for j in range(len(mat[0])):
        for k in range(len(mat)):
            result[j][k] = mat[k][j]
    return result


def multiply_matrix(mat, matrix_size, con):
    matrix = list()
    for i in range(matrix_size[0]):
        a = list()
        for j in range(matrix_size[1]):
            a.append(mat[i][j] * int(con))
        matrix.append(a)
    return matrix


def determinant(mat):
    n = len(mat)
    temp = [0] * n
    total = 1
    det = 1

    for i in range(0, n):
        index = i

        while mat[index][i] == 0 and index < n:
            index += 1
        if index == n:
            continue
        if index != i:
            for j in range(0, n):
                mat[index][j], mat[i][j] = mat[i][j], mat[index][j]
            det = det * int(pow(-1, index - i))
        for j in range(0, n):
            temp[j] = mat[i][j]
        for j in range(i + 1, n):
            num1 = temp[i]
            num2 = mat[j][i]
            for k in range(0, n):
                mat[j][k] = (num1 * mat[j][k]) - (num2 * temp[k])
            total = total * num1
    for i in range(0, n):
        det = det * mat[i][i]
    return det / total


def add_matrix(matrix_1, matrix_2, matrix_1_size, matrix_2_size):
    matrix = list()
    if (matrix_1_size[0], matrix_1_size[1]) == (matrix_2_size[0], matrix_2_size[1]):
        for i in range(matrix_1_size[0]):
            matrix_sum = list()
            for j in range(matrix_1_size[1]):
                matrix_sum.append(matrix_1[i][j] + matrix_2[i][j])
            matrix.append(matrix_sum)
        print_matrix(matrix)

    else:
        print("ERROR")


def multiply_matrices(mat1, mat2):
    result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*mat2)] for X_row in mat1]
    return result


def co_factor_3(mat):
    result = [[0 for x in range(len(mat))] for y in range(len(mat[0]))]
    result[0][0] = (mat[3 - 2][3 - 2] * mat[3 - 1][3 - 1]) - (mat[3 - 2][3 - 1] * mat[3 - 1][3 - 2])
    result[0][1] = -((mat[3 - 2][3 - 3] * mat[3 - 1][3 - 1]) - (mat[3 - 2][3 - 1] * mat[3 - 1][3 - 3]))
    result[0][2] = (mat[3 - 2][3 - 3] * mat[3 - 1][3 - 2]) - (mat[3 - 2][3 - 2] * mat[3 - 1][3 - 3])

    result[1][0] = -((mat[3 - 3][3 - 2] * mat[3 - 1][3 - 1]) - (mat[3 - 3][3 - 1] * mat[3 - 1][3 - 2]))
    result[1][1] = (mat[3 - 3][3 - 3] * mat[3 - 1][3 - 1]) - (mat[3 - 3][3 - 1] * mat[3 - 1][3 - 3])
    result[1][2] = -((mat[3 - 3][3 - 3] * mat[3 - 1][3 - 2]) - (mat[3 - 3][3 - 2] * mat[3 - 1][3 - 3]))

    result[2][0] = (mat[3 - 3][3 - 2] * mat[3 - 2][3 - 1]) - (mat[3 - 3][3 - 1] * mat[3 - 2][3 - 2])
    result[2][1] = -((mat[3 - 3][3 - 3] * mat[3 - 2][3 - 1]) - (mat[3 - 3][3 - 1] * mat[3 - 2][3 - 3]))
    result[2][2] = (mat[3 - 3][3 - 3] * mat[3 - 2][3 - 2]) - (mat[3 - 3][3 - 2] * mat[3 - 2][3 - 3])
    return result


def co_factor_2(mat):
    result = [[0 for x in range(len(mat))] for y in range(len(mat[0]))]
    result[0][0] = mat[1][1]
    result[0][1] = -(mat[1][0])
    result[1][0] = -(mat[0][1])
    result[1][1] = mat[0][0]
    return result


def inverse(mat):
    array = np.linalg.inv(mat)
    print_matrix(array.tolist())


def init():
    menu = int(input("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a Determinant
6. Inverse matrix
0. Exit
Your choice:"""))
    if menu == 0:
        exit()
    else:
        if menu == 1:
            ma, mas = take_matrix()
            na, nas = take_matrix()
            add_matrix(ma, na, mas, nas)

        elif menu == 2:
            ma, mas = take_matrix()
            constant = input("Enter constant number:")
            result = multiply_matrix(ma, mas, constant)
            print_matrix(result)

        elif menu == 3:
            ma, mas = take_matrix()
            na, nas = take_matrix()
            result = multiply_matrices(ma, na)
            print_matrix(result)

        elif menu == 4:
            transpose_menu = int(input("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice:"""))
            if transpose_menu == 1:
                ma, mas = take_matrix()
                result = main_transpose(ma)
                print_matrix(result)

            elif transpose_menu == 2:
                ma, mas = take_matrix()
                result = side_transpose(ma)
                print_matrix(result)

            elif transpose_menu == 3:
                ma, mas = take_matrix()
                result = vertical_transpose(ma)
                print_matrix(result)

            elif transpose_menu == 4:
                ma, mas = take_matrix()
                result = horizontal_transpose(ma)
                print_matrix(result)

        elif menu == 5:
            ma, mas = take_matrix()
            result = determinant(ma)
            print(result)

        elif menu == 6:
            ma, mas = take_matrix()
            inverse(ma)
        init()


while True:
    init()

