import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
result = 0
queue = deque()
length_count = [0 for _ in range(21)]
for _ in range(N):
    temp = input().rstrip()
    if len(queue) == K + 1:
        length_count[len(queue.popleft())] -= 1
    
    queue.append(temp)
    result += length_count[len(temp)]
    length_count[len(temp)] += 1

print(result)