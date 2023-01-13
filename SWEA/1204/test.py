from collections import Counter

case = int(input())
for x in range(1, case+1):
    order = input()
    test = list(map(int, input().split()))
    cnt = Counter()
    for number in test:
        cnt[number] += 1
    answer = cnt.most_common(1)[0][0]
    print(f'#{order} {answer}')
