import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
area = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    area[a].append(b)

visited = [False for _ in range(N+1)]

dp = [N*2 for _ in range(N+1)]

stack = deque()
stack.append(X)
visited[X] = True
dp[X] = 0

while stack:
    # print(stack)
    cur = stack.popleft()
    for item in area[cur]:
        dp[item] = min(dp[item] ,dp[cur] + 1)
        if not visited[item]:
            stack.append(item)
            visited[item] = True
# print(dp)
cnt = 0
for i in range(1, N+1):
    if dp[i] == K:
        print(i)
    else:
        cnt += 1
if cnt == N:
    print(-1)

