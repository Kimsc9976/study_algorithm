import sys
input = sys.stdin.readline
n, m= map(int, input().split())
memo = { k : v for k, v in (input().split() for _ in range(n))}
print(*[memo[item] for item in (input().rstrip() for _ in range(m))], sep='\n')