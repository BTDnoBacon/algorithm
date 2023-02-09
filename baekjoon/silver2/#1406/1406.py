import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

start_string = list(input().rstrip())
temp_li = deque()
M = int(input())
for _ in range(M):
    command = input()
    if 'L' in command:
        if len(start_string) == 0:
            continue
        temp_li.appendleft(start_string.pop())

    elif 'D' in command:
        if len(temp_li) == 0:
            continue
        start_string.append(temp_li.popleft())
        
    elif 'B' in command:
        if len(start_string) == 0:
            continue
        start_string.pop()

    else:
        string = list(map(str,command.split()))[1]
        start_string.append(string)

while temp_li:
    start_string.append(temp_li.popleft())

print(''.join(start_string))