import sys
input = sys.stdin.readline

from collections import deque

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        locations = []

        for _ in range(n + 2):  # 집 + 편의점들 + 도착지
            x, y = map(int, input().split())
            locations.append((x, y))

        # BFS
        queue = deque()
        visited = [False] * (n + 2)

        queue.append(0)  # 집에서 시작
        visited[0] = True

        while queue:
            current = queue.popleft()
            for i in range(n + 2):
                if not visited[i] and manhattan(locations[current], locations[i]) <= 1000:
                    visited[i] = True
                    queue.append(i)

        print("happy" if visited[-1] else "sad")
solve()