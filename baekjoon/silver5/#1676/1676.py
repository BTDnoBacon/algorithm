import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

temp = 0
result = 0

for i in range(1, 500):
    temp = N // 5**i
    if temp == 0:
        break
    result += temp



print(result)
