import sys
import collections
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
# print(N, K)

case = list(map(int, input().split()))
# print(case)

count = 0


def merge_sort(case):
    mid = (len(case)-1) // 2
    # print(mid)
    if len(case) > 1:
        temp_A = collections.deque(merge_sort(case[:mid+1]))
        temp_B = collections.deque(merge_sort(case[mid+1:]))
    else:
        return collections.deque(case)

    return merge(temp_A, temp_B)
    


def merge(temp_A, temp_B):
    temp = []
    global count

    while temp_A and temp_B:
        if temp_A[0] <= temp_B[0]:
            temp.append(temp_A.popleft())
            # print(temp)

            count += 1
            if count == K:
                print(temp[-1])
            
        elif temp_A[0] > temp_B[0]:
            temp.append(temp_B.popleft())
            count += 1
            # print(temp)

            if count == K:
                print(temp[-1])
         

    
    while temp_A:
        temp.append(temp_A.popleft())
        count += 1
        if count == K:
            print(temp[-1])
    while temp_B:
        temp.append(temp_B.popleft())
        count += 1
        if count == K:
            print(temp[-1])
    
    return temp

        
merge_sort(case)

if count < K:
    print(-1)

