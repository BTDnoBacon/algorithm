import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
import collections

N, M = list(map(int, input().split()))

answer_string = ''
graph = collections.defaultdict(set)
top_length = 0
length = 0
# visited = [False for _ in range(N+1)]
for _ in range(M):
    x, y = list(map(int, input().split()))
    graph[y].add(x)


# print(graph)
def bfs(graph, node):
    count = 0
    visited = [False for _ in range(N+1)]
    queue = collections.deque()
    queue.append(node)

    while queue:
        n = queue.popleft()
        if visited[n] != True:
            visited[n] = True
            queue += graph[n]
            count += 1

    return count

for i in range(1, N+1):
    length = bfs(graph, i)
    if top_length < length:
        top_length = length
        answer_string = f'{i} '
    elif top_length == length:
        answer_string += f'{i} '

print(answer_string)


