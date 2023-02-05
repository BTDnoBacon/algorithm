import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())

case = list(map(int, input().split()))

temp = [0 for _ in range(N)]
def merge(a_case, b_case):

    i = 0
    j = 0
    while True:
        # print(temp)
        if i == len(a_case) or j == len(b_case):
            break

        if a_case[i] <= b_case[j]:
            temp[i+j] = a_case[i]
            i += 1
            continue
        else:
            temp[i+j] = b_case[j]
            j += 1
            continue

        
    while i != len(a_case):
        temp[i+j] = a_case[i]
        i += 1
    

    while j != len(b_case):
        temp[i+j] = b_case[j]
        j += 1

    return temp[:len(a_case)+len(b_case)]


def merge_sort(case):
    l = len(case)
    if l == 1:
        return case

    a_case = merge_sort(case[:l//2])
    b_case = merge_sort(case[l//2:])
    
    return merge(a_case, b_case)


print(merge_sort(case)[K-1])
# print(case[1])