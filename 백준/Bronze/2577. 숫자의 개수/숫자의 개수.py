A = int(input())
B = int(input())
C = int(input())

prod = str(A*B*C)
ans = [0 for _ in range(10)]
for c in prod:
    ans[int(c)] += 1

print(*ans, sep='\n')
    