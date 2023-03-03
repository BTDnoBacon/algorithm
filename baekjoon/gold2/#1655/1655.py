import sys
import heapq
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
max_heap = list()
min_heap = list()


for _ in range(N):
    number = int(input())

    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -number)
    
    else:
        heapq.heappush(min_heap, number)

    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        left = -heapq.heappop(max_heap)
        right = heapq.heappop(min_heap)

        heapq.heappush(max_heap, -right)
        heapq.heappush(min_heap, left)

    print(-max_heap[0])
