import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

queue = [0 for _ in range(14)]

front = 0
back = 0

for i in range(N):
    user_input = input()

    if 'push' in user_input:
        push_int = int(user_input.split()[1])
        queue[back] = push_int
        back += 1

    elif 'front' in user_input:
        if queue[front] == 0:
            print(-1)
        else:
            print(queue[front])

    elif 'back' in user_input:
        if queue[back - 1] == 0:
            print(-1)
        else:
            print(queue[back - 1])
    
    elif 'size' in user_input:
        print(back - front)

    elif 'empty' in user_input:
        if back - front == 0:
            print(1)
        else:
            print(0)

    else:
        if queue[front] == 0:
            print(-1)
        else:
            print(queue[front])
            queue[front] = 0
            front += 1    