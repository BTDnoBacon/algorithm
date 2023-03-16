import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def makesegment(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = (makesegment(start, mid, idx * 2) * makesegment(mid+1, end, idx * 2 + 1))%1000000007
    return tree[idx]

def interval(start, end, idx, left, right):
    if left > end or right < start:
        return 1
    
    if left <= start and right >= end:
        return tree[idx]

    mid = (start + end)//2

    return (interval(start, mid, idx * 2, left, right) * interval(mid+1, end, idx*2 +1, left, right))%1000000007

def update(start, end, idx, what, value):
    if what < start or what > end:
        return
    

    if start == end:
        tree[idx] = value
        # tree[idx] //= arr[what]
        return
    mid = (start + end) // 2
    update(start, mid, idx*2, what, value)
    update(mid+1, end, idx*2 +1, what, value)
    tree[idx] = tree[2*idx] * tree[2*idx + 1] %1000000007


N, M, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]
tree = [0 for _ in range(N * 4)]
# print(arr)
makesegment(0, N-1, 1)

# print(tree)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, N-1, 1, b-1, c)
        # arr[b-1] = c
        # print(tree)
        # print(arr,'-----')
    else:
        print(interval(0, N-1, 1, b-1, c-1)%1000000007)