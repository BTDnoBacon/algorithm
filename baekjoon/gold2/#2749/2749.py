import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())

matrix = [[1, 1], [1, 0]]



def reminder(li):
    for item in li:
        item[0] = item[0] % 1000000
        item[1] = item[1] % 1000000

    return li

def fibo(n):
    if n == 0:
        return matrix
    if n == 1:
        return matrix

    li = fibo(n//2)
    if li[0][0] > 1000000:
        li = reminder(li)
    temp = []
    temp.append([li[0][0]*li[0][0] + li[0][1]*li[1][0], li[0][0]*li[0][1]+ li[0][1]*li[1][1]])
    temp.append([li[1][0]*li[0][0] + li[1][1]*li[1][0], li[1][0]*li[0][1]+ li[1][1]*li[1][1]])
    # print(n)
    # print(temp)
    if n % 2:
        return [[temp[0][0] + temp[0][1], temp[0][0]],[temp[1][0] + temp[1][1], temp[1][0]]]
    else:
        return temp

# print(n)
# print(fibo(5))
# result = fibo(3)
print(fibo(n-1)[0][0]%1000000)

