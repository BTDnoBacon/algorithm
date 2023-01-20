import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

S_set = set()

for _ in range(N):
    S_set.add(input().rstrip())

count = 0
for _ in range(M):
    if input().rstrip() in S_set:
        count += 1

print(count)
