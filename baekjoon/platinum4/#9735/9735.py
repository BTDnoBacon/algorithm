import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    A, B, C, D = list(map(int, input().split()))

    s = -10**6
    l = 10**6
    while s <= l:
        mid = (s+l)//2
        