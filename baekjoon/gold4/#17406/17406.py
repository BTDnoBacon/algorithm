import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def rotation_matrix(r, c, s):
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
        rotation_matrix(r, c, s-1)
    

    

N, M, K = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
for _ in range(K):
    r, c, s = map(int, input().split())
    rotation_matrix(r-1, c-1, s)

min_value = 100 * M + 1
for item in matrix:
    sum_items = sum(item)
    if sum_items < min_value:
        min_value = sum_items
print(min_value) 
