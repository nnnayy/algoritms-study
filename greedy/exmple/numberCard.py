#!/usr/bin/python
# -*- coding: latin-1 -*-

# 입력받는 배열에는 두 가지 경우가 있다고 가정한다.
# 3 x 3
# 3 1 2 / 4 1 4 / 2 2 2

# 2 x 4
# 7 3 1 8 / 3 3 3 4

n, m = map(int, input().split())

result = 0

for i in range(n): # 행이 기준
    data = list(map(int, input().split()))
    min_num = min(data)
    result = max(result, min_num)

print(result)