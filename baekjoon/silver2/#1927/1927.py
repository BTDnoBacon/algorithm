import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def enque(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    while p > 0 and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2
    return

def deque():
    global last
    tree[1], temp = tree[last], tree[1]
    tree[last] = 0
    last -= 1
    # print(tree, last)

    p = 1
    while True:
        # print(tree)
        if p > last:
            break
        c_left = p * 2
        c_right = p * 2 + 1
        
        if tree[c_left] and tree[c_right]:
            if (tree[c_left] < tree[c_right]) and tree[p] > tree[c_left]:
                tree[c_left], tree[p] = tree[p], tree[c_left]
                p = c_left
            elif (tree[c_left] > tree[c_right]) and tree[p] > tree[c_right]:
                tree[c_right], tree[p] = tree[p], tree[c_right]
                p = c_right
            continue
        if tree[c_right] and tree[p] > tree[c_right]:
            tree[c_right], tree[p] = tree[p], tree[c_right]
            p = c_right
            continue
        if tree[c_left] and tree[p] > tree[c_left]:
            tree[c_left], tree[p] = tree[p], tree[c_left]
            p = c_left
            continue
        break
    return temp
        

        



N = int(input())

tree = [0 for _ in range(N)]
last = 0
for _ in range(N):
    dummy = int(input())
    if dummy == 0:
        if last == 0:
            print(0)
        else:
            print(deque())
    else:
        enque(dummy)
    # print(tree)