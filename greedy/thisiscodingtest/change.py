# 거슬러 줘야 할 돈이 1260원이라고 가정하자.
import sys
input = sys.stdin.readline

money = 1260 # 거스름돈
changes = 0 # 동전의 개수

coins = [500, 100, 50, 10] # 동전의 형식을 배열로 선언

for coin in coins:
    changes += (money//coin) # changes에 몫을 저장
    money %= coin # money에 나머지를 저장

print(changes) # 6을 출력
