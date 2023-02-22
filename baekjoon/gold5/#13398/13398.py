import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
case = list(map(int, input().split()))

for i in range(1, n):
    case[i] += case[i-1]
print(case)