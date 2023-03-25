import sys
# sys.stdin = open('input.txt', 'r')
import heapq
input = sys.stdin.readline


N = int(input())
heap = []
li = [list(map(int, input().split())) for _ in range(N)]
li.sort()

heapq.heappush(heap, li[0][1])  #첫번째 강의가 끝나는 시간을 넣음
for i in range(1, N):
    if heap[0] > li[i][0]:
        heapq.heappush(heap, li[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, li[i][1])
# print(heap)
print(len(heap))