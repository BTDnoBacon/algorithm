import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

import math

N = int(input())

case = list(map(int, input().split()))
# print(case)

for i in range(1, N):
    gcd_num = math.gcd(case[0], case[i])
    print(f'{case[0]//gcd_num}/{case[i]//gcd_num}')