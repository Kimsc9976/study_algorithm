import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = set(input().rstrip() for _ in range(n))
b = set(input().rstrip() for _ in range(m))
r = sorted(d & b)
print(len(r))
print(*r, sep='\n')
