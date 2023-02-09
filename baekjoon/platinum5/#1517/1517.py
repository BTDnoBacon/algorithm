import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
case = list(map(int,input().split()))
# print(N, case)

Swap = 0

def merge_sort(case):
    mid = len(case) // 2
    if len(case) == 1:
        return case
    else:
        merge(merge_sort(case[:mid]), merge_sort(case[mid:]))


def merge(case_one, case_two):
    temp = []
    
    pass


print(Swap)
