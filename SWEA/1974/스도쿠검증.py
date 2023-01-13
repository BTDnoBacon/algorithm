import os
f = open('./input (2).txt')

# case = int(input())
for num in range(1, 2):
    test_case = []
    check = -1
    for i in range(9):
        test_case.append(list(map(int, f.readline().split())))
        
    for i in range(9):
        if len(set(test_case[i])) != 9:
            check = 0

    for i in range(9):
        col_set = []
        for j in range(9):
            col_set.append(test_case[j][i])
        if len(set(col_set)) != 9:
            check = 0

    for i in range(3):
        sqr_set = []
        for j in range(3):
            sqr_set = sqr_set + test_case[j][i*3:i*3 +3]
        if len(set(sqr_set)) != 9:
            check = 0


    for i in range(3):
        sqr_set = []
        for j in range(3,6):
            sqr_set = sqr_set + test_case[j][i*3:i*3 +3]
        if len(set(sqr_set)) != 9:
            check = 0

    for i in range(3):
        sqr_set = []
        for j in range(6,9):
            sqr_set = sqr_set + test_case[j][i*3:i*3 +3]
        if len(set(sqr_set)) != 9:
            check = 0

    if check == -1:
        check = 1

    print(check)
