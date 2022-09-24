import sys
input = sys.stdin.readline

# 380
# pay = 1000 - 380 = 640
# 1 1 0 4

# 1 4 1 4 1 4

money = int(input()) # 지불할 돈

pay = 1000-money # 잔돈

coins = [500, 100, 50, 10, 5, 1]

count = 0

for coin in coins:
    count += (pay//coin)
    pay %= coin

print(count)