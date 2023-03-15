N,M,D = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

animys = []

def is_finish():
  global animys
  animys = []
  Trigger = True
  for j in range(M):
    for i in range(N-1,-1,-1):
      if play[i][j] == 1:
        animys.append((i,j))
        Trigger = False

  return True if Trigger else False

from itertools import combinations

new_line = [[0] * M]
result = 0
for bows in combinations(range(M), 3):
  play = [arr[:] for arr in matrix]
  
  kill = 0
  while not is_finish():
    
    targets = set()
    for bow in bows:
      
      _min = N+M
      target = None
      
      for x,y in animys:
        length = abs(N-x) + abs(bow-y)
        if length <= D:
          if length < _min: # 왼쪽부터 가니까 중복고려할 필요업음
            _min = length
            target = (x,y)
      
      
      if target : targets.add(target)
    kill += len(targets)
    
    # 타겟들은 죽었습니다..
    for target in targets:
      if not target : continue
      play[target[0]][target[1]] = 0
    play = new_line + play
    play.pop()
  
  result = result if result > kill else kill

print(result)
      
    