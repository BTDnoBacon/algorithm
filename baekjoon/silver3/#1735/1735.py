import sys
import math
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

A, B = map(int, input().split())
C, D = map(int, input().split())

upper = A * D + B * C
down = B * D

gcd = math.gcd(upper, down)

print(upper//gcd, down//gcd)