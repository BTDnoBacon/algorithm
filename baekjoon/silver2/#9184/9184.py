import sys
from collections import defaultdict
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


dp_dict = defaultdict(int)
# print(dp_dict)
def dp(input_li, dp_dict):
    if dp_dict[input_li] > 0:
        return dp_dict[input_li]
    
    a = input_li[0]
    b = input_li[1]
    c = input_li[2]

    if  a<= 0 or b <= 0 or c <= 0:
        dp_dict[input_li] = 1
        return dp_dict[input_li]
    elif a > 20 or b > 20 or c > 20:
        return dp((20, 20, 20), dp_dict)
    elif  a < b and b < c:
        dp_dict[input_li] = dp((a, b, c-1), dp_dict) + dp((a, b-1, c-1), dp_dict) - dp((a, b-1, c), dp_dict)
        return dp_dict[input_li]
    else:
        dp_dict[input_li] = dp((a-1, b, c), dp_dict) + dp((a-1, b-1, c), dp_dict) + dp((a-1, b, c-1), dp_dict) - dp((a-1, b-1, c-1), dp_dict)
        return dp_dict[input_li]




while True:
    input_li = tuple(map(int, input().split()))
    if input_li[0] == input_li[1] == input_li[2] == -1:
        break

    print(f'w{input_li} =',dp(input_li, dp_dict))