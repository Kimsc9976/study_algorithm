a, b = map(int, input().split())
A = min(a, b)
B = max(a, b)

if (A == B) or ((A + 1) == B) :
    print(0)
    print()
else:
    cnt = B - A - 1
    print(cnt)
    print(*range(A+1, B))