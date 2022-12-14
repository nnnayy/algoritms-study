# Greedy Algorithms

## 예제 3-1

- 문제 : 500원, 100원, 50원, 10원이 무한으로 존재하고, 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라.
- 조건 : 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

## 실전문제 1

- 문제 : 배열의 크기 N, 숫자가 더해지는 횟수 M, K가 주어질 때 큰 수의 법칙에 따른 결과를 출력하라.
- 입력 조건 :

* 첫째 줄에 N(2<= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
* 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단 각각의 자연수는 1이상 10000 이하의 수로 주어진다.
* 입력으로 주어지는 K는 항상 M보다 작거나 같다.

- 출력 조건 :

* 첫째 줄은 큰 수에 법칙에 따라 더해진 답을 출력한다.

## 실전문제 2

- 문제 : 카드들이 N \* M 형태로 놓여 있을 때, 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 프로그램을 만들어라.
- 조건 :

* 숫자가 쓰인 카드들이 N \* M 형태로 놓여 있다. 이때 N은 행의 개수, M은 열의 개수를 의미한다.
* 먼저 뽑고자 하는 카드가 포함된 행을 선택한다.
* 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
* 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 항에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

- 입력 조건 :

* 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다.(1 <= N, M <= 100)
* 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10000 이하의 자연수이다.

- 출력 조건 :

* 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

## 실전문제 3

- 문제 : 어떤 수 N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하라.
- 조건 :

* N에서 1을 뺀다.
* N을 K로 나눈다.

- 입력 조건 :

* 첫째 줄에 N(2 <= N <= 100000)과 K(2 <= K <= 100000)가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.

- 출력 조건 :

* 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.
