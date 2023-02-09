import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())


def isPalindrome(test_case, l, r, count):
    count += 1
    if l == r or l > r:
        return [1, count]
    elif test_case[l] == test_case[r]:
        return isPalindrome(test_case, l+1, r-1, count)
    elif test_case[l] != test_case[r]:
        return [0, count]

for _ in range(T):
    count = 0
    test_case = list(input().rstrip())
    r = len(test_case)-1
    l = 0
    # print(test_case)
    print(*isPalindrome(test_case, l, r, count))
