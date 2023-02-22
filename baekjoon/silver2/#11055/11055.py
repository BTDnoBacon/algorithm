import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input().rstrip())
case = list(map(int,input().split()))

dp = [0 for _ in range(N+1)]
dp[0] = case[0]

for i in range(1, N):
    for j in range(i):
        if case[i] > case[j]:
            dp[i] = max(dp[i], dp[j] + case[i])
        else:
            dp[i] = max(dp[i], case[i])

print(max(dp))