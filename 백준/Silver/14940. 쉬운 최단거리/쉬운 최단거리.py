import sys
input = sys.stdin.readline

from collections import deque


n, m= map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
rlt =[[-1 for _ in range(m)] for _ in range(n)]

def bfs(a, b):
    
    d = ((0,-1), (0,1), (-1,0), (1,0))
    que = deque([(a,b, 0)])
    rlt[a][b] = 0
    
    while que:
        x, y, depth = que.popleft()
        
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            
            if not (0 <= nx < n and 0 <= ny < m) : continue
            if matrix[nx][ny] == 0 : continue
            if rlt[nx][ny] != -1 : continue
            
            rlt[nx][ny] = depth + 1
            que.append((nx,ny, rlt[nx][ny]))

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            rlt[i][j] = 0
        elif matrix[i][j] == 2:
            bfs(i,j)
            
for i in range(n):
    print(*rlt[i])