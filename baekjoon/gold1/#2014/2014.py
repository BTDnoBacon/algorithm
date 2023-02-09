import sys
import collections
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

K, N = map(int, input().split())

case = list(map(int, input().split()))

queue = collections.deque()
for item in case:
    queue.append(item)

# print(queue)


