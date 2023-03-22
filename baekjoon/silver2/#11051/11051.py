import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())

import math

result = math.comb(N, K) % 10007

print(result)