import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    clothes = dict()  # key: 종류, value: 해당 종류 개수
    
    for _ in range(N):
        a, b = input().strip().split()
        
        # 종류별 개수 카운팅
        clothes[b] = clothes.get(b, 0) + 1
        
    result = 1
    
    # 각 종류마다 (입는다 + 안 입는다) 선택이 존재
    # => (count + 1)
    for count in clothes.values():
        result *= (count + 1)
        
    # 모든 종류에서 "아무것도 안 입는 경우" 1개 제외
    print(result - 1)