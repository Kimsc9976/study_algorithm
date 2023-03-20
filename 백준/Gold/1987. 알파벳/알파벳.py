N, M = map(int,input().split())

texts = [list(map(lambda x: ord(x) - 65, input())) for _ in range(N)]

is_used = [False]*26

ans = 0

dx = (1,-1,0,0)
dy = (0,0,1,-1)
def bt(start, length):
    global ans

    for k in (0,1,2,3):
        nx = start[0] + dx[k]
        ny = start[1] + dy[k]
        if nx<0 or ny<0 or nx>=N or ny>=M: continue
        if is_used[texts[nx][ny]]: continue
        is_used[texts[nx][ny]] = True
        length += 1
        bt((nx,ny), length)
        is_used[texts[nx][ny]] = False
        length -= 1
    
    
    ans = max(ans,length)

is_used[texts[0][0]] = True
bt((0,0), 1)
print(ans)