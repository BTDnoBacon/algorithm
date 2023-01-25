import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

import collections

n = int(input())

stack_list = collections.deque([i for i in range(1, n+1)])
# print(stack_list)
stack = []
stack.append(stack_list.popleft())
print_list = ['+']
check = True
for _ in range(n):
    # print(stack)
    user_input = int(input())
    while True:
        if len(stack) == 0 or user_input > stack[-1]:
            stack.append(stack_list.popleft())
            print_list.append('+')
            continue
        elif user_input == stack[-1]:
            stack.pop()
            print_list.append('-')
            break
        elif user_input < stack[-1]:
            check = False
            break
    if check == False:
        break

if check == False:
    print('NO')
else:
    for item in print_list:
        print(item)
