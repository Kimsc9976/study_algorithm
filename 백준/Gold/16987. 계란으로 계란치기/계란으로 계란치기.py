N = int(input())

eggs = [list(map(int,input().split())) for _ in range(N)]

ans = 0

def check():
    cnt = 0
    for egg in eggs:
        if egg[0] <= 0:
            cnt += 1
    
    return cnt

def dfs(now):
    global ans
    if now == N:
        ans = max(ans, check())
        return
    
    stiff, weight = eggs[now]
    if stiff<=0:
        dfs(now+1)
    else:
        is_all_broken = True
        for i in range(N):
            if now != i and eggs[i][0] > 0:
                is_all_broken = False
                eggs[now][0] = stiff - eggs[i][1]
                eggs[i][0] = eggs[i][0] - weight
                dfs(now + 1)
                eggs[now][0] = stiff
                eggs[i][0] = eggs[i][0] + weight
        if is_all_broken:
            dfs(N)
    pass


dfs(0)
print(ans)