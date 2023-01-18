import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

import collections

N = int(input().rstrip())

matrix = [list(map(int, list(input().rstrip()))) for _ in range(N)]

house = []

def bfs(x, y, matrix):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = collections.deque()
    visited = []
    queue.append([x, y])
    visited.append([x, y])
    while queue:
        x, y = queue.popleft()
        matrix[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                continue
            elif matrix[nx][ny] == 1 and [nx, ny] not in visited:
                queue.append([nx, ny])
                visited.append([nx, ny])
        
    return len(visited)

    
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            house.append(bfs(i, j, matrix))
        

house.sort()

print(len(house))
for row in house:
    print(row)
