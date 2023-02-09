import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

li = [0 for _ in range(N+1)]

if N > 0:
    li[1] = 1

if N > 1:
    li[2] = 2
    
if N > 2:
    for i in range(3, N+1):
        li[i] = (li[i-1] + li[i-2])%15746

print(li[N])