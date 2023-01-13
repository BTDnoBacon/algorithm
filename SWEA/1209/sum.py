import os
f = open('./sum.txt')
# print(f.readline())
for i in range(10):
    case = int(f.readline())
    test_case = []
    top_value = 0
    sum = 0

    for i in range(100):
        test_case.append(list(map(int, f.readline().split())))

    for i in range(len(test_case)):
        sum = 0
        for j in range(len(test_case[i])):
            sum += test_case[i][j]
        if top_value < sum:
            top_value = sum

    for i in range(len(test_case)):
        sum = 0
        for j in range(len(test_case)):
            sum += test_case[j][i]
        if top_value < sum:
            top_value = sum


    sum = 0
    for i in range(len(test_case)):
        sum += test_case[i][i]
    if top_value < sum:
        top_value = sum
        sum = 0
    else:
        sum = 0



    for i in range(len(test_case)):
        sum += test_case[i][99-i]
    if top_value < sum:
        top_value = sum
    # print(top_value)
    print(f'#{case} {top_value}')
