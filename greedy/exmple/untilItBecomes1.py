#!/usr/bin/python
# -*- coding: latin-1 -*-

# 입력값으로 25 5가 주어진다고 가정하자.

n, k = map(int, input().split())

result = 0

while n >= k:
    while n%k != 0:
        n -= 1
        result += 1

    n = n//k
    result += 1

print(result)

