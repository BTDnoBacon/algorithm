import sys
sys.stdin = open('input2.txt', 'r')
input = sys.stdin.readline

import collections

N, M = list(map(int, input().split()))

matrix = [list(map(int, list(input().rstrip()))) for _ in range(N)]

# print(matrix)

def bfs(x, y, matrix):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = collections.deque([[x, y]])
    visited = [[False for _ in range(M)] for _ in range(N)]
    # print(queue)
    # print(visited)
    while queue:
        print(matrix)
        # print(count)
        # print(queue)
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                continue
            # elif matrix[nx][ny] == 0 :
            #     continue
            elif matrix[nx][ny] == 1 and not visited[nx][ny]:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])
                visited[nx][ny] = True


    return matrix[N-1][M-1]
    # print(visited)
    
print(bfs(0, 0, matrix))
