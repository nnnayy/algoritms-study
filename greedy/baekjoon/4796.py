import sys
input = sys.stdin.readline

# 캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가를 시작했다
# l : 5 / 5 
# p : 8 / 8
# v: 20 / 17
# result = 14 / 11
# 8 8 4 / 8 8 1
# 5 5 4 / 5 5 1
# 연속하는p=8일 중, l=5일 동안만 사용할 수 있고, v=20일짜리 휴가를 시작했다

count = 0
days = []

while True:
    count += 1
    l, p, v = map(int, input().split())

    if (v == 0) and (p == 0) and (l == 0):
        break

    result = l * (v//p) + (v%p)
    days.append(result)


for i in range(count):
    print(f"case {i+1}: {days[i]}")