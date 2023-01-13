import sys
sys.stdin = open('./숫자배열회전.txt', 'r')

N = int(input())

for order in range(1, N+1):
    matrix =[]
    K = int(input())
    for i in range(K):
        matrix.append(list(map(str, input().split())))

    matrix_3 = [[row[len(matrix)-i-1] for row in matrix] for i in range(len(matrix))]
    matrix_2 = [[row[len(matrix)-i-1] for row in matrix_3] for i in range(len(matrix))]
    matrix_1 = [[row[len(matrix)-i-1] for row in matrix_2] for i in range(len(matrix))]

    matrix_3 = list(map(''.join, matrix_3))
    matrix_2 = list(map(''.join, matrix_2))
    matrix_1 = list(map(''.join, matrix_1))

    print(f'#{order}')
    for i in range(len(matrix)):
        print(f'{matrix_1[i]} {matrix_2[i]} {matrix_3[i]}')