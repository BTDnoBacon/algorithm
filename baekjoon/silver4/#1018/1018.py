import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N, M = map(int, input().split())

# print(N, M)

matrix = [list(input().rstrip()) for _ in range(N)]
min_value = 1557
# print(matrix)
ans_matrix_B = [[] for _ in range(8)]
ans_matrix_W = [[] for _ in range(8)]

for i in range(8):
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0:
                ans_matrix_B[i].append('B')
                ans_matrix_W[i].append('W')
            else:
                ans_matrix_B[i].append('W')
                ans_matrix_W[i].append('B')

    else:
        for j in range(8):
            if j % 2 == 0:
                ans_matrix_W[i].append('B')
                ans_matrix_B[i].append('W')
            else:
                ans_matrix_W[i].append('W')
                ans_matrix_B[i].append('B')

# print(ans_matrix_B)
# print(ans_matrix_W)


def BW_check(input, i, j):
    count_B = 0
    count_W = 0
    for a in range(8):
        for b in range(8):
            if matrix[i+a][j+b] != ans_matrix_B[a][b]:
                count_B +=1
            elif matrix[i+a][j+b] != ans_matrix_W[a][b]:
                count_W +=1
    count = min(count_B, count_W)
    return count


for i in range(N-7):
    for j in range(M-7):
        min_value = min(min_value, BW_check(matrix[i][j], i, j))

print(min_value)