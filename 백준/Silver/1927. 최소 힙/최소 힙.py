import sys
input = sys.stdin.readline
import heapq

n= int(input())

arr = list()
for _ in range(n):
    target = int(input())
    
    if target == 0:
        print(0 if len(arr) == 0 else heapq.heappop(arr))
    else:
        heapq.heappush(arr, target)