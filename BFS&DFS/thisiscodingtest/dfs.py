# dfs : 깊이 우선 탐색 알고리즘
# 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 알고리즘

# dfs는 스택 자료구조를 이용함
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
# 2. 스택의 최상단 노드에 방문하지 않은 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다.
# 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

def dfs(graph, v, visited):
    visited[v] = True # 현재 노드를 방문 처리함
    print(v, end=" ") # %는 왜 생기는지?

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],# 왜 비워두는 거야?
    [2, 3, 8], # 1번 노드와 연결된 노드
    [1, 7], # 2번 노드와 연결된 노드
    [1, 4, 5], # 3번 노드와 연결된 노드
    [3, 5], # 4번 노드와 연결된 노드
    [3, 4], # 5번 노드와 연결된 노드
    [7], # 6번 노드와 연결된 노드
    [2, 6, 8], # 7번 노드와 연결된 노드
    [1, 7] # 8번 노드와 연결된 노드
]

# 각 노드가 방문된 정보를 1차원 리스트 자료형으로 표현
visited = [False] * 9

# 정의된 dfs 함수 호출
dfs(graph, 1, visited)