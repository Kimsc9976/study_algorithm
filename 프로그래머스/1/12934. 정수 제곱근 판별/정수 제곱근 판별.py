import math

def solution(n):
    # 1. 제곱근 구하기
    sqrt_n = math.sqrt(n)
    
    # 2. 정수 판별 (제곱근의 소수부가 0인지)
    if sqrt_n.is_integer():
        # 3. 정수라면 (sqrt+1)^2
        return int(pow(sqrt_n + 1, 2))
    else:
        # 4. 정수가 아니라면 -1
        return -1