import sys
sys.stdin = open('./input.txt', 'r')

import math

N = int(input()) - 1
case = 10**N + 1
lastCase = 1003

while case < lastCase:
    input = case
    for j in range(N):
        for i in range(2, int(math.sqrt(input))):
            if input == 1:
                break
            if input % i > 0:
                break
        input = input//10

    if input == 2 or 3 or 5 or 7:
        print()
    case += 2


# def primeNumber(input):
#     for i in range(2, int(math.sqrt(input))):
#         if input == 1:
#             break
#         if input % i > 0:
#             break

#     if input//10 > 0:
#         print(input//10)
#         primeNumber(input//10)
#     if input//10 == 0:
#         print('--')
#         return 1

# input = case
# print(primeNumber(input))

# while case <= lastCase:
#     input = case
#     if primeNumber(input) == 1:
#         print(case)
#     case = case + 2

