from collections import deque

def solution(queue1, queue2):
    answer = 0
    originA = deque(queue1)
    originB = deque(queue2)
    queueA = deque(queue1)
    queueB = deque(queue2)
    maxA = max(queue1)
    maxB = max(queue2)

    sum_A = sum(queueA)
    sum_B = sum(queueB)
    half_sum = sum_A + sum_B
    if half_sum % 2 > 0:
        return -1
    half_sum //= 2
    if half_sum < maxA or half_sum < maxB:
        return -1
    check = True
    while check:
        if half_sum == sum_A:
            break
        elif half_sum < sum_A:
            dummy = queueA.popleft()
            sum_A -= dummy
            sum_B += dummy
            queueB.append(dummy)
        else:
            dummy = queueB.popleft()
            sum_A += dummy
            sum_B -= dummy
            queueA.append(dummy)
        answer += 1
        if answer > 0 and (len(queueA) == 0 or len(queueB) == 0 or originA == queueA or originB == queueB or answer > 700000) :
            check = False
    
    if check:
        return answer
    else:
        return -1



print(solution([3, 2, 7, 2], [4, 6, 5, 1]))

