import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
case = list(map(int, input().split()))

heap = []
for _ in range(K):
    heapq.heappush(heap, 0)

print(heap)

for item in case:
    print(heap)
    heapq.heappush(heap, heapq.heappop(heap) + item)

print(heap)