import sys
input = sys.stdin.readline

n = int(input())
data = { idx : False for idx in range(21) }

def calc(target, idx):
    global data
    if target == 'add':
        data[idx] = True
    elif target == 'remove':
        data[idx] = False
    elif target == 'check':
        print(1 if data[idx] else 0)
    elif target == 'toggle':
        data[idx] = False if data[idx] else True
    elif target == 'all':
        data = { i : True for i in range(21) }
    elif target == 'empty':
        data = { i : False for i in range(21) }

for i in range(n):
    t = input().split()
    if len(t) == 1:
        calc(t[0], 0)
    else :
        calc(t[0], int(t[1]))
