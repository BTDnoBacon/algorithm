import sys
import heapq
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

card = list()


for _ in range(N):
    heapq.heappush(card, int(input()))



result = 0

while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    temp = a + b
    result += temp
    heapq.heappush(card, temp)

print(result)