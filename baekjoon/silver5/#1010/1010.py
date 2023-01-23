import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())

import math

for _ in range(T):
    a, b = map(int, input().split())
    print(math.comb(b, a))