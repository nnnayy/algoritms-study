# 인접 행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
# 인접 리스트 : 리스트로 그래프의 연결 관게를 표현하는 방식

INF = 999999999 # 연결이 되어 있지 않은 노드끼리는 무한의 비용으로 작성 # 논리적으로 큰 값을 999999999으로 초기화

adjacency_matrix = [ # 2차원 리스트를 이용해 인접 행렬을 표현
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

# 인접 행렬 : 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비됨


adjacency_list = [[] for _ in range(3)] # 행이 3개인 2차원 리스트로 인접 리스트 표현

adjacency_list[0].append((1, 7)) # (노드, 거리)
adjacency_list[0].append((2, 5))

adjacency_list[1].append((0, 7))

adjacency_list[2].append((0, 5))

# 인접 리스트 : 연결된 정보만을 저장해 메모리를 효율적으로 사용함, 두 노드가 연결되어 있는지 정보를 얻는 속도가 느림

print(f"인접 행렬 : {adjacency_matrix}")
print(f"인접 리스트 : {adjacency_list}")