import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

# 중복 제거 후 정렬
sorted_unique = sorted(set(num_list))

# 각 값에 대해 압축된 좌표를 딕셔너리에 저장
num_dict = {value: idx for idx, value in enumerate(sorted_unique)}

# 원래 리스트의 값들을 압축된 값으로 변환
rlt = [num_dict[num] for num in num_list]

print(*rlt)