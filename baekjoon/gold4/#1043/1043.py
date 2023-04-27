# 1043 거짓말
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

truth = set(input().split()[1:])

party = [set(input().split()[1:]) for _ in range(M)]

for _ in range(M):
    for item in party:
        if item.intersection(truth):
            truth = truth.union(item)


result = 0
for item in party:
    if not item.intersection(truth):
        result += 1

print(result)