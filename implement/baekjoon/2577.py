# 2022 9/29 성공

import sys
input = sys.stdin.readline

data = [int(input()) for _ in range(3)]
numbers = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

sum = 1

for i in data:
    sum *= i #17037300

for j in str(sum):
    numbers[j] += 1

for k in numbers:
    print(numbers[k])