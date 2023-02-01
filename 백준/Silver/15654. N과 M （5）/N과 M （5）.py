import sys

N, M = map(int, sys.stdin.readline().split()) 
num_lst = sorted(list(map(int, sys.stdin.readline().split())))

lst = num_lst.copy()
def NM(target):
  
  is_used = list()
  def bt(is_used):
    if len(is_used) == M:
      print(*is_used)
      return
    
    for i in target:
      if i in is_used:
        continue
      is_used.append(i)
      bt(is_used)
      is_used.pop()
  bt(is_used)

NM(lst)