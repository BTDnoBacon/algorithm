import sys
from collections import deque

sys.stdin = open('./input.txt', 'r')

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= 16 or ny < 0 or ny >= 16:
                continue

            if graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

            if graph[nx][ny] == 3:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return 0

for i in range(10):
    N = int(input())
    graph = []
    start = tuple()

    for j in range(16):
        graph.append(list(map(int, input())))

    for k in range(16):
        if 3 in graph[k]:
            end = (k, graph[k].index(3))

    print(f'#{N}', bfs(1, 1))




