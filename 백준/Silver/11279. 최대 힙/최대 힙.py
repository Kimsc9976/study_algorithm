import sys
import heapq
input = sys.stdin.readline

n = int(input())

num_list = []
# print(num_list)

for _ in range(n):
    target = int(input())
    if target == 0:
        if num_list:
            print(heapq.heappop(num_list) * -1)
        else:
            print(0)
        pass
    else :
        heapq.heappush(num_list, target*-1)