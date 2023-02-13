import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

test_str = list(input().rstrip())
bomb_str = list(input().rstrip())
bomb_length = len(bomb_str)
# print(bomb_length)
stack = []

# print(test_str[-bomb_length:])

for item in test_str:
    stack.append(item)

    # print(stack[-bomb_length:], bomb_str)
    if stack[-bomb_length:] == bomb_str:
        for _ in range(bomb_length):
            stack.pop()
            # print(stack)

# print(stack)

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))