import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())

# print(N, K)

import collections

answer = []
queue = collections.deque()
for i in range(1, N+1):
    queue.append(i)

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())

    answer.append(queue.popleft())

print(f'<{", ".join(str(row) for row in answer)}>')
