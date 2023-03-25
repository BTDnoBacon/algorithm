import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())

case = [input().rstrip() for _ in range(N)]
dict_alpha = defaultdict(int)

for item in case:
    for i in range(len(item)):
        dict_alpha[item[i]] += 10 ** (len(item) - i - 1)
# print(dict_alpha)

num_li = sorted(dict_alpha.values(), reverse=True)

result = 0
temp = 9
for item in num_li:
    result += item*temp
    temp -= 1
print(result)
