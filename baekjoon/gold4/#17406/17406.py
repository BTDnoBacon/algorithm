import sys
from itertools import permutations
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def rotation_matrix(r, c, s, matrix):
    temp = matrix[r-s][c-s]
    for j in range(c-s, c+s):
        matrix[r-s][j+1], temp = temp, matrix[r-s][j+1]
    for i in range(r-s, r+s):
        matrix[i+1][c+s], temp = temp, matrix[i+1][c+s]
    for j in range(c+s, c-s, -1):
        matrix[r+s][j-1], temp = temp, matrix[r+s][j-1]
    for i in range(r+s, r-s, -1):
        matrix[i-1][c-s], temp = temp, matrix[i-1][c-s]
    
    if s - 1 > 0:
        rotation_matrix(r, c, s-1, matrix)
    

    

N, M, K = map(int, input().split())

case = [list(map(int, input().split())) for _ in range(N)]
dummy = []
for _ in range(K):
    r, c, s = map(int, input().split())
    dummy.append([r, c, s])
    # rotation_matrix(r-1, c-1, s)
dummy = list(permutations(dummy))
# print(dummy)
min_value = 100 * M + 1
for item in dummy:
    matrix = []
    for row in case:
        matrix.append(row[:])
    for r, c, s in item:
        rotation_matrix(r-1, c-1, s, matrix)
    for item in matrix:
        min_value = min(min_value, sum(item))

print(min_value)


# for item in matrix:
#     sum_items = sum(item)
#     if sum_items < min_value:
#         min_value = sum_items
# print(min_value) 
