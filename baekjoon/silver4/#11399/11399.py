import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
case = list(map(int, input().split()))
case.sort()
result = 0

for i in range(N):
    result += case[i] * (N-i)
print(result)