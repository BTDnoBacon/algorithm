import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin

N = int(input())


stack = [0 for _ in range(10000)]
pointer = -1

for _ in range(N):
    # print(stack)
    # print(pointer)
    user_input = input()
    if 'push' in user_input:
        pointer +=1
        # print('push')
        stack[pointer] = int(user_input.split()[1])
    elif 'top' in user_input:
        # print('top')
        # print(stack)
        if stack[pointer] == 0:
            print(-1)
        else:
            print(stack[pointer])
    elif 'size' in user_input:
        # print('size')
        print(pointer + 1)
    elif 'empty' in user_input:
        # print('empty')
        if stack[pointer] == 0 :
            print(1)
        else:
            print(0)
    elif 'pop' in user_input:
        # print('pop')
        if stack[pointer] == 0:
            print(-1)
        else:
            print(stack[pointer])
            stack[pointer] = 0
            pointer = pointer - 1
