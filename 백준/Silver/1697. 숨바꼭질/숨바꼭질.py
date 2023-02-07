from collections import deque
N, K = map(int,input().split())

que = deque()
cnt = 0
# def bfs(start,depth):
#   global cnt
#   deq.append((start, depth))
  
#   while len(deq):
#     now, dep = deq.popleft()
    
#     l = now - 1
#     deq.append((l,dep+1))
#     r = now + 1
#     deq.append((r,dep+1))
#     t = now * 2
#     deq.append((t,dep+1))
    
#     if l == K or r == K or t == K:
#       cnt = dep + 1
#       break
#       break
dx = [1, -1, 2]

arr = [0] * (10**6 + 1)
def bfs(start, target):
  global arr
  
  isVisited = [False] * (10**6 + 1)
  
  que.append(start)
  isVisited[start] = True
  arr[start] = 0
  
  while que:
    now = que.popleft()
    now_time = arr[now]
    
    if now == target:
      return now_time
    
    for t in range(3):
      if t == 2:
        nx = now * 2
        if nx >= 2*100000:
          continue
        if isVisited[nx]:
          continue
        if nx < -1:
          continue
        que.append(nx)
        isVisited[nx] = True
        arr[nx] = now_time + 1
      else:
        nx = now + dx[t]
        if nx >= 2*100000:
          continue
        if nx < -1:
          continue
        if isVisited[nx]:
          continue
        que.append(nx)
        isVisited[nx] = True
        arr[nx] = now_time + 1
      
  

answer = bfs(N, K)
print(answer)
