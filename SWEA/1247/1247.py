import sys
sys.stdin = open('input.txt', 'r')

import collections



N = int(input())
for _ in range(N):
    M = int(input())
    dummy = list(map(int, input().split()))
    print(dummy)
