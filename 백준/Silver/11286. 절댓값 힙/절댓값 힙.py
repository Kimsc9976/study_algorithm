import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if heap:
            # 가장 작은 절댓값 + 실제 값이 작은 원소 pop
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        # (절댓값, 실제값)을 기준으로 push
        heapq.heappush(heap, (abs(x), x))