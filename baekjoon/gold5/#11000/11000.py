import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
li.sort(key=lambda a: a[0])
li.sort(key=lambda a: a[1])
queue = deque()
for item in li:
    queue.append(item)

count = 0

# print(queue)
while queue:
    temp = deque()
    length = len(queue)
    s = 0
    l = 0
    for _ in range(length):
        cur_s, cur_l = queue.popleft()
        if cur_s >= l:
            l = cur_l
        else:
            temp.append([cur_s, cur_l])
    count += 1
    if len(temp) > 0:
        queue = temp

print(count)
