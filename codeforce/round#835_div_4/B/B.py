import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = set(map(ord, input().rstrip()))
    print(max(s)-96)