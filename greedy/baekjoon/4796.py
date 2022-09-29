import sys
input = sys.stdin.readline

# 캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가를 시작했다
# l : 5 / 5 
# p : 8 / 8
# v: 20 / 17
# result = 14 / 11
# 8 8 4 / 8 8 1
# 5 5 4 / 5 5 1

count = 0

while True:
    l, p, v = map(int, input().split())

    days = [v, p, l]

    count += 1

    if (v == 0) and (p == 0) and (l == 0):
        break

    for day in days:
        result = l * (v//p) + (v%p)

    print(f"case {count}: {result}")