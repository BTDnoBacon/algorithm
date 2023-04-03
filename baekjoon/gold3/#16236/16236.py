import sys
from collections import deque
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  # 상하좌우

def bfs(x, y):
    global baby
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[x][y] = 1
    queue = deque()
    temp = list()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            elif area[nx][ny] > baby:
                continue
            elif not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
                if 0 < area[nx][ny] < baby:
                    temp.append([nx, ny, visited[nx][ny] - 1])
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))



N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
baby = 2

for i in range(N):
    for j in range(N):
        if area[i][j] == 9:
            x, y = i, j
            area[i][j] = 0

# print(bfs(x, y))

cnt = 0
result = 0
while True:
    fish = bfs(x, y)
    if len(fish) == 0:
        break

    nx, ny, distance = fish.pop()
    result += distance
    area[nx][ny] = 0
    x, y = nx, ny
    cnt += 1
    if cnt == baby:
        cnt = 0
        baby += 1

print(result)