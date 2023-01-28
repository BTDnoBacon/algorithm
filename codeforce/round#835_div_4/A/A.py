import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    test_case = list(map(int, input().split()))
    test_case.sort()
    print(test_case[1])