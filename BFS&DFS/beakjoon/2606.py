import sys
input = sys.stdin.readline

from collections import deque

cnt = 0 # 바이러스에 걸리는 컴퓨터의 수

v = int(input()) # 컴퓨터의 개수 = 정점의 개수
e = int(input()) # 연결선 개수 = 간선의 개수

graph = [[]*(v+1) for _ in range(v+1)] # 그래프 초기화
visited = [0]*(v+1) # 방문한 컴퓨터인지 확인

for i in range(e): # 그래프 만들기
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = 1 # True
q = deque([1])

while q:
    c = q.pop()

    for x in graph[c]:
        if visited[x] == 0:
            q.append(x)
            visited[x] = 1
            cnt += 1

print(cnt)