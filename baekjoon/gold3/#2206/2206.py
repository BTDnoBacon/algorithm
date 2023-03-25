import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



N, M = map(int, input().split())

area = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append([0, 0, True])
visited[0][0] = 1

while queue:
    # print(queue)
    x, y, check = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
            continue
        elif (not visited[nx][ny] or visited[x][y]+1 < visited[nx][ny]) and check:
            if area[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny, False])
            else:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny, True])
        elif not visited[nx][ny] or visited[x][y]+1 < visited[nx][ny]:
            if area[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny, False])

# print(visited)
if visited[N-1][M-1] != 0:
    print(visited[N-1][M-1])
else:
    print(-1)



