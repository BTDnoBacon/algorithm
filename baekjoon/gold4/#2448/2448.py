# 2448번 별찍기

import sys
input = sys.stdin.readline

N = int(input())


def recursion(k):
    if k == 3:
        return ['  *  ', ' * * ', '*****']
    temp = []
    li = recursion(k//2)

    for item in li:
        temp.append(' '*(k//2) + item + ' '*(k//2))

    for item in li:
        temp.append(item + ' ' + item)

    return temp

print('\n'.join(recursion(N)))


