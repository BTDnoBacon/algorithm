import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, M = map(int,input().split())

A_set = set(map(int,input().split()))
B_set = set(map(int,input().split()))

print(len(set.union(A_set, B_set)) - len(set.intersection(A_set, B_set)))