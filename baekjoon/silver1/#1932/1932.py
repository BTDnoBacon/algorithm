import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
case = [list(map(int, input().split())) for _ in range(n)]
# print(case)

