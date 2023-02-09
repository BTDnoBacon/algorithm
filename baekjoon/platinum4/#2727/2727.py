import sys
import math
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())

li = []

def recursion(N, R,b):
    a = 0
    if N == 1:
        # li.append([a, b])
        return
    elif N == 0:
        return

    N = N + R
    # if len(li) == 0:
    while (2 ** a) < N:
        a += 1
    li.append([a-1, b])
    N = N - (2 ** (a-1))
    N1 = N//3
    R = N%3
    b += 1
    recursion(N1, R,b)
    # recursion((N - N//3), b)


    return li    


    



    



for tc in range(1, T+1):
    N = int(input())
    print(tc)
    idx = 0
    # a = 0
    b = 0
    print(recursion(N, 0,b))