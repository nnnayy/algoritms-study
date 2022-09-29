# 2022 9/29 성공

import sys
input = sys.stdin.readline

data = [int(input()) for _ in range(9)]

max_num = 0
count = 0

for i in data:
    count += 1
    if max(data) == i:
        max_num = i
        break

print(max_num)
print(count)