import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


S = input().rstrip()

idx = 0
length = len(S)
check = False
stack = []
while idx < length:
    stack.append(S[idx])
    if S[idx] == ' ':
        stack.pop()
        while stack:
            print(stack.pop(), end='')
        print(' ',end='')
    
    
    if S[idx] == '<':
        stack.pop()
        while stack:
            print(stack.pop(), end='')
        check = True
        print('<', end='')
    while check:
        idx += 1
        print(S[idx], end='')
        if S[idx] == '>':
            check = False
    
    idx += 1

while stack:
    print(stack.pop(), end='')