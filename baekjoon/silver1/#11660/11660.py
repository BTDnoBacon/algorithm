import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int ,input().split())

matrix = [list(map(int ,input().split())) for _ in range(N)]

pre_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        pre_sum[i][j] = pre_sum[i-1][j] + pre_sum[i][j-1] - pre_sum[i-1][j-1] + matrix[i-1][j-1]

# 구간합 구하기
for _ in range(M):
    # (x1,y1) ~ (x2,y2) 합 구하기
    x1, y1, x2, y2 = map(int,input().split())
    print(pre_sum[x2][y2] - pre_sum[x1-1][y2] - pre_sum[x2][y1-1] + pre_sum[x1-1][y1-1])