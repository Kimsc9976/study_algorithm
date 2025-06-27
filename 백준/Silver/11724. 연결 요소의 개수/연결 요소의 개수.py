import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m= map(int, input().split())

node = [ [] for _ in range(n+1)]
is_visited = [ False for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

# print(node)

def dfs(start, is_visited):
    if is_visited[start]:
        return 0
    
    is_visited[start] = True
    
    for idx in node[start]:
        dfs(idx, is_visited)
        
    return 1
cnt = 0
for i in range(1, n+1):
    cnt += dfs(i, is_visited)

print(cnt)