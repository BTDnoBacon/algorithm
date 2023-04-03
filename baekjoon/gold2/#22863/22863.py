import sys

input = sys.stdin.readline

N, K = map(int, input().split())
P = [0] + list(map(int, input().split()))
D = [0] + list(map(int, input().split()))

visited = [False for _ in range(N+1)]
dp = [0 for _ in range(N)]
for i in range(1, N+1):
    if not visited[i]:
        temp = [i]
        nxt = temp[-1]
        visited[nxt] = True
        while True:
            if not visited[D[nxt]]:
                visited[D[nxt]] = True
                temp.append(D[nxt])
                nxt = temp[-1]
            else:
                break

        length = len(temp)

        for i in range(length):
            dp[temp[(K+i)%length] - 1] = P[temp[i]]



print(*dp)
