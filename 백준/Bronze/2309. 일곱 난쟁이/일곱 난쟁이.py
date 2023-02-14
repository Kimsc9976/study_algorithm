nanj = list()
for _ in range(9):
    nanj += [int(input())]

lst = []
def dfs(depth, lst : list):
    if depth == 7:
        return True if sum(lst) == 100 else False
    
    for i in range(depth, len(nanj)):
        if nanj[i] in lst: continue
        
        lst.append(nanj[i])
        check = dfs(depth+1,lst)
        if check == True :
            return check
        lst.pop()
        

dfs(0,lst)
print(*sorted(lst),sep='\n')