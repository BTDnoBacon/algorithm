import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
case = list(map(int, input().split()))

dp = [0 for _ in range(N)]
dp[0] = 1

for i in range(1, N):
    dp[i] = 1
    for j in range(i):
        if case[j] < case[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))