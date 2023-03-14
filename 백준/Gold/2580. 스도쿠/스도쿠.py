sudoku = [list(map(int,input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i,j))
            
def checkRow(x, a):
    for i in range(9):
        if a == sudoku[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == sudoku[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == sudoku[nx+i][ny+j]:
                return False
    return True

def bt(idx):
    global blank
    if idx == len(blank):
        for row in sudoku:
            print(*row)
        return True

    needs = getnum(blank[idx])
    
    for need in needs:
        x = blank[idx][0]
        y = blank[idx][1]
        if checkRow(x,need) and checkCol(y,need) and checkRect(x,y,need):
            sudoku[x][y] = need
            trigg = bt(idx+1)
            if trigg:
                return True
            sudoku[x][y] = 0
    
def getnum(item):
    x,y = item

    row_set = [ False for _ in range(10)]
    for j in range(9):
        row_set[sudoku[x][j]] = True

    col_set = [ False for _ in range(10)]
    for i in range(9):
        col_set[sudoku[i][y]] = True
    
    need = set()
    for a in range(1,10):
        if row_set[a] == False:
            need.add(a)    
        if col_set[a] == False:
            need.add(a)

    return need

bt(0)