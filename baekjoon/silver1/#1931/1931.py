import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
li.sort(key=lambda a: a[0])
li.sort(key=lambda a: a[1])

count = 0
s = 0
l = 0
idx = 0

for item in li:
    cur_s, cur_l = item
    if cur_s >= l:
        l = cur_l
        count += 1

print(count)