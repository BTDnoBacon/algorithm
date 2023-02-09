import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
# print(N)

def recursion(k):
    if k == 1:
        return ['*']
    temp = []
    star_list = recursion(k//3)

    for item in star_list:
        temp.append(item*3)

    for item in star_list:
        temp.append(item+' '*(k//3)+item)

    for item in star_list:
        temp.append(item*3)
 
    return temp

print('\n'.join(recursion(N)))