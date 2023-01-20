import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

test_set = set()
input_string = input().rstrip()

# print(len(input_string))

for i in range(len(input_string)):
    for j in range(len(input_string)):
        if i+j > len(input_string):
            break
        test_set.add(input_string[i:i+j])

print(len(test_set))