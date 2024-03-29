N = int(input())
numbers = list(map(int, input().split()))
oper = list(map(int, input().split()))

min = +1e9
max = -1e9

def devide(a,b):
  rlt = int(a//b) if a*b >= 0 else -1 * int(abs(a)//abs(b))
  return rlt


def dfs(i, compare):  
    global oper, min, max # 전역변수 등록해야 업데이트 됨
    if(sum(oper) == 0):
        if(compare > max):
            max = int(compare)
        if(compare<min):
            min = int(compare)
        return
    
    if(oper[0]>0):
        oper[0] -= 1
        dfs(i+1, compare + numbers[i])
        oper[0] += 1
        
    if(oper[1]>0):
        oper[1] -= 1
        dfs(i+1, compare - numbers[i])
        oper[1] += 1
        
    if(oper[2]>0):
        oper[2] -= 1
        dfs(i+1, compare * numbers[i])
        oper[2] += 1
        
    if(oper[3]>0):
        oper[3] -= 1
        dfs(i+1, devide(compare,numbers[i]))
        oper[3] += 1    

dfs(1,numbers[0])
print(int(max))
print(int(min))
