import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

case = [0 for _ in range(10001)]
for _ in range(N):
    case[int(input())] += 1


for i in range(10001):
    if case[i] == 0:
        continue

    while case[i] > 0:
        print(i)
        case[i] -= 1
    