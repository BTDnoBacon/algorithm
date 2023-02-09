import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    user_input = list(input().rstrip())
    left_li = []
    right_li = deque()

    for item in user_input:
        if item == '>':
            if len(right_li) == 0:
                continue
            left_li.append(right_li.popleft())

        elif item == '<':
            if len(left_li) == 0:
                continue
            right_li.appendleft(left_li.pop())

        elif item == '-':
            if len(left_li) == 0:
                continue
            left_li.pop()

        else:
            left_li.append(item)

    while right_li:
        left_li.append(right_li.popleft())

    print(''.join(left_li))