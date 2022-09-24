import sys
input = sys.stdin.readline

l, p, v = map(int, input().split())

days = [v, p, l]

# 캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가를 시작했다
# l : 5 / 5 
# p : 8 / 8
# v: 20 / 17
# result = 14 / 11
# 8 8 4 / 8 8 1
# 5 5 4 / 5 5 1

result  = 0
count = 0

for day in days:
    result = l * (v//p) + (v%p)
    count += 1

    if day == 0:
        break

print(f"case{count}: {result}")