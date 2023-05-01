
N, M, K = map(int,input().split())

fire_balls = dict()
distances = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
# matrix = [[-1 for _ in range(N+2)]] + [[-1] + [0 for _ in range(N)] + [-1] for _ in range(N)] + [[-1 for _ in range(N+2)]]
matrix = [ [0 for _ in range(N)] for _ in range(N)]
for i in range(M):
  r, c, m, s, d = map(int,input().split())
  matrix[r-1][c-1] = m
  fire_balls[i] = [(r-1,c-1),s,d, m]
  
# print(len(fire_balls))



def step1(idx, F_ball):

  (x,y), s, d, m = fire_balls[F_ball]
  nx = (x + distances[d][0] * s)%N
  ny = (y + distances[d][1] * s)%N
  
  fire_balls[idx] = [(nx,ny),s,d, m]
  
  if not at_same_pos.get((nx,ny)):
    at_same_pos.setdefault((nx,ny), [])
  at_same_pos[(nx,ny)] += [idx]
  


def check_d(s):
    all_even = all(element % 2 == 0 for element in s)
    all_odd = all(element % 2 != 0 for element in s)
    return all_even or all_odd

def step2():

  cnt = 0
  new_fire_balls = dict()
  for x, y in at_same_pos:
    total_mass = 0
    total_speed = 0
    total_direct = set()
    items = at_same_pos[(x,y)]
    for item in items:
      (r,c),s,d,m = fire_balls[item]
      total_mass += m
      total_speed += s
      total_direct.add(d)
    
    if len(items) == 1:
      new_fire_balls[cnt] = [(x,y), s, d, m]
      cnt += 1
    else:
      new_mass = total_mass//5 
      if new_mass == 0 : continue 
      new_speed = total_speed//len(items)
      new_d = (0,2,4,6) if check_d(total_direct) else (1,3,5,7)

      for a in range(4):
        new_fire_balls[cnt] = [(x,y), new_speed, new_d[a], new_mass]
        cnt += 1
  
  return new_fire_balls


for _ in range(K):
  if len(fire_balls) == 0: break
  
  at_same_pos = dict()
  for idx, fire_ball in enumerate(fire_balls):
    step1(idx, fire_ball)
    
  fire_balls = step2()
ans = 0
for key, value in fire_balls.items():
  ans += value[-1]
print(ans)