import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

case = list(map(int, input().split()))

acc_sum = [0 for _ in range(N+1)]
for idx in range(1, N+1):
    acc_sum[idx] += acc_sum[idx-1] + case[idx-1]

# print(acc_sum)

for _ in range(M):
    i, j = map(int, input().split())
    i = i - 1
    print(acc_sum[j] - acc_sum[i])

