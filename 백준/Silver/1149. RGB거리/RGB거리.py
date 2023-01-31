import sys

N = int(sys.stdin.readline())

ans = [[0 for _ in range(3)] for _ in range(N)]

for i in range(N):
  RGB = list(map(int,sys.stdin.readline().split()))
  if i == 0:
    ans[i][0] = RGB[0]
    ans[i][1] = RGB[1]
    ans[i][2] = RGB[2]
  else:
    ans[i][0] = min(ans[i-1][1],ans[i-1][2]) + RGB[0]
    ans[i][1] = min(ans[i-1][0],ans[i-1][2]) + RGB[1]
    ans[i][2] = min(ans[i-1][0],ans[i-1][1]) + RGB[2]
    
print(min(ans[N-1]))