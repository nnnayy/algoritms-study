# N = 5, M = 8, K = 3
# 5개의 숫자를 입력받고, 총 8번 더하며, 같은 숫자는 세번까지 연속될 수 있다.
# 입력받은 자연수 2 4 5 4 6

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split()) # 공백으로 숫자를 나누어 각 변수에 넣어준다.
numbers = list(map(int, input().split())) # 공백으로 숫자를 나누고 리스트에 넣어준다.

numbers.sort() # 숫자 정렬
first = numbers[-1] # 가장 큰 수
second = numbers[-2] # 두번 째로 큰 수

result = 0 # 결과값
count = 1 # k의 숫자를 세는 변수


while m != 0: # 8번만 숫자를 더하도록 설정
    for count in range(k): # 같은 숫자는 세 번만 연속되도록 설정
        if count != k:
            result += first
            count += 1
            m -= 1
    if count == k:
        count = 0
        result += second
        m -= 1

print(result) # 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5