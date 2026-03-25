import sys
input = sys.stdin.readline

N, X = map(int, input().split())
lst = list(map(int, input().split()))


print(*(item for item in lst if item < X))