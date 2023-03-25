import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
answer = 0
import math


def extended_gcd(a, b):
    if a == 0:
        return 0, 1
    else:
        x, y = extended_gcd(b % a, a)
        return y - (b // a) * x, x



for _ in range(N):
    K, C = map(int, input().split())
    if math.gcd(K, C) != 1:
        print('IMPOSSIBLE')
        continue
    # elif K == 1 and C != 1:
    #     print(1)
    #     continue
    elif C == 1 and K+1 > 10**9:
        print('IMPOSSIBLE')
        continue
    elif C == 1:
        print(K+1)
        continue

    if K == 1:
        print(1)
        continue
    else:
        answer = extended_gcd(C, K)[0]
        if answer > 10**9:
            print('IMPOSSIBLE')
        else:
            print(((answer%K)+K)%K)


