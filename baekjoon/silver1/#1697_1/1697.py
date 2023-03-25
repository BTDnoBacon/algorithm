# import sys
# from collections import deque
# # sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

# N, K = map(int, input().split())
# visited = [False for _ in range(K + 10)]
# queue = deque()
# queue.append([N, 0])
# min_cnt = 213213132
# while queue:
#     print(queue)
#     cur_val, cur_cnt = queue.popleft()
#     if cur_val == K:
#         # min_cnt = min(min_cnt, cur_cnt)
#         print(cur_cnt)
#         break
#     if 0 <= cur_val + 1 < K + 9 and not visited[cur_val+1]:
#         visited[cur_val+ 1] = True
#         queue.append([cur_val+1, cur_cnt+1])
#     if 0 <= cur_val - 1 < K + 9 and not visited[cur_val-1]:
#         visited[cur_val - 1] = True
#         queue.append([cur_val-1, cur_cnt+1])
#     if 0 <= cur_val * 2 < K + 9 and not visited[cur_val*2]:
#         visited[cur_val*2] = True
#         queue.append([cur_val*2, cur_cnt+1])
# print(min_cnt)


import sys
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                q.append(next_v)


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
array = [0] * MAX
print(bfs(n))