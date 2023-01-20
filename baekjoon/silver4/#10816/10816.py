import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

import collections

count_dict = collections.Counter()

for item in N_list:
    count_dict[item] += 1

for element in M_list:
    print(count_dict[element], end=' ')