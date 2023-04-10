import sys
input = sys.stdin.readline

def Find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x

def Union(x, y):
    rep[Find_set(y)] = Find_set(x)

V, E = map(int, input().split())

rep = [i for i in range(V+1)]
link = list()
for _ in range(E):
    link.append(list(map(int, input().split())))
link.sort(key=lambda x:x[2])
# print(link)

MST = 0
for item in link:
    x, y, w = item
    if Find_set(x) != Find_set(y):
        Union(x, y)
        MST += w

print(MST)