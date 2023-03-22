import sys
input = sys.stdin.readline

N = int(input())

hp = [0] + list(map(int, input().split()))
happy = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(100)] for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, 100):
        if j >= hp[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-hp[i]] + happy[i])
        else:
            dp[i][j] = dp[i-1][j]
# print(dp)
for item in dp:
    print(item)
# print(dp[N][99])
