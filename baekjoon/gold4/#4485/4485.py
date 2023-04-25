import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = 1000000000
idx = 0

while True:
    N = int(input())
    idx += 1
    if N == 0:
        break

    area = [list(map(int, input().split())) for _ in range(N)]
    visited = [[INF for _ in range(N)] for _ in range(N)]
    visited[0][0] = area[0][0]

    queue = deque()
    queue.append([0, 0])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            elif visited[nx][ny] > visited[x][y] + area[nx][ny]:
                visited[nx][ny] = visited[x][y] + area[nx][ny]
                queue.append([nx, ny])

    print(f'Problem {idx}:', visited[N-1][N-1])