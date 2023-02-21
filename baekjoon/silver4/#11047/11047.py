import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
stack = []

for _ in range(N):
    coin = int(input())
    if coin <= M:
        stack.append(coin)

count = 0
while M > 0:
    cur_coin = stack.pop()
    div = M // cur_coin
    count += div
    M -= div * cur_coin

print(count)