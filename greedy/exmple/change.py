#!/usr/bin/python
# -*- coding: latin-1 -*-

# 예제 3-1
# 문제 : 500원, 100원, 50원, 10원이 무한으로 존재하고, 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라.
# 조건 : 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

# 거슬러 줘야 할 돈이 1260원이라고 가정하자.

money = 1260 # 거스름돈
changes = 0 # 동전의 개수

coins = [500, 100, 50, 10] # 동전의 형식을 배열로 선언

for coin in coins:
    changes += (money//coin) # changes에 몫을 저장
    money %= coin # money에 나머지를 저장

print(changes) # 6을 출력
