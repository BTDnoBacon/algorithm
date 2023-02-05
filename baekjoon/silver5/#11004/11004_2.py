import sys
from collections import defaultdict
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())

case = list(map(int, input().split()))

# max_value = max(case)

count = defaultdict(int)

for item in case:
    count[item] += 1

print(count.keys())

for key in count.keys():
    K -= count[key]
    if K <= 0:
        print(key)
        break