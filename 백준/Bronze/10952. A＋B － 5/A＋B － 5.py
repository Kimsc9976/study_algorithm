import sys

while True:
    try:
        A, B = list(map(int, sys.stdin.readline().split()))
        if(A == 0 and B == 0):
            break
        print(A + B)
    except:
        break