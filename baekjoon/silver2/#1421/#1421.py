import sys
sys.stdin = open('input.txt', 'r')

N, M, K = list(map(int, input().split()))

case = list()
for _ in range(N):
    case.append(int(input()))

print(case)