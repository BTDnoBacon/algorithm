import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    A, B, C, D = map(int, input().split())
    # print(A, B, C, D)
    if D == 0:
        alpha = 0

    for temp in range(1, 1000001):
        if D == 0:
            break
        if temp == 0 or D % temp:
            continue
        else:
            if (A*(temp**3)) + (B * (temp**2)) + (C*temp) + D == 0:
                alpha = temp
                break
            elif A*(-temp)**3 + B * (-temp)**2 + C* (-temp) + D == 0:
                alpha = (-temp)
                break


    a = A
    b = A*alpha + B
    c = b*alpha + C
    Discriminant = b**2 - 4*a*c
    # print(a, b, c)
    answer = set()

    if Discriminant >= 0:
        beta = (-b - Discriminant**(1/2))/2 / A
        gamma = (-b + Discriminant**(1/2))/2 / A

        answer.add(alpha)
        answer.add(beta)
        answer.add(gamma)
        answer = list(answer)
        answer.sort()

    else:
        answer.add(alpha)

    result = []
    # for item in answer:
    #     result.append(f'{item:.4f}')
    print(*answer)