H, W = map(int,input().split())

column = list(map(int,input().split()))

idx = 0
max_H = 0
for i, col in enumerate(column):
    if max_H <= col:
        idx = i
        max_H = col

Hole = 0
target = column[0]
for i in range(idx):
    if target < column[i]:
        target = column[i]
    elif target > column[i]:
        Hole += (target - column[i])


target = column[-1]
for i in range(W-1,-1,-1):
    if target < column[i]:
        target = column[i]
    elif target > column[i]:
        Hole += (target - column[i])
    if column[idx] == target:
        break


print(Hole)