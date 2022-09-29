import sys
input = sys.stdin.readline

# 가로행, 세로열
# 행은 위에서 아래로, 열은 왼쪽에서 오른쪽으로 증가

n = int(input())
x, y = 1, 1 # x는 가로, y는 세로
moves = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D'] # (0, -1) (0, 1) (-1, 0) (1, 0)

for move in moves:

    for i in range(len(move_types)):
    
        if move == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
            if nx < 1 or ny < 1 or nx > n or ny > n:
                continue
    
            x, y = nx, ny

print(x, y)