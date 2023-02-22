import sys

input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(N+1)]

dp[0] = -1

for i in range(1, N+1):
    if i % 3 and i % 2:
        dp[i] = dp[i-1] + 1
    elif i % 3:
        dp[i] = min(dp[i//2], dp[i-1]) + 1
    elif i % 2:
        dp[i] = min(dp[i//3], dp[i-1]) + 1
    else:
        dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1

print(dp[N])