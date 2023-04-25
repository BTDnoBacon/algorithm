import sys
input = sys.stdin.readline

N = int(input())
case = list(map(int, input().split()))

dummy = sorted(list(set(case)))
another = dict()
for i in range(len(dummy)):
    another[dummy[i]] = i
# print(dummy)
dp = [0 for _ in range(N)]
for i in range(N):
    dp[i] = another[case[i]]

print(*dp)
