import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
import collections

N, M = list(map(int, input().split()))

answer_string = ''
top_length = 0
length = 0
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = list(map(int, input().split()))
    graph[y].append(x)


# print(graph)
def bfs(node):
    count = 0
    visited = [False for _ in range(N+1)]
    queue = collections.deque([node])
    visited[node] = True

    while queue:
        n = queue.popleft()
        for y in graph[n]:
            if not visited[y]:
                visited[y] = True
                queue.append(y)
                count += 1
        # print(queue)
    return count

for i in range(1, N+1):
    length = bfs(i)
    if top_length < length:
        top_length = length
        answer_string = f'{i} '
    elif top_length == length:
        answer_string += f'{i} '

print(answer_string)


