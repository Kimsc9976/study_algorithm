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



####ㅇ 이전에 있던 병신같은 코드
import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
num_dict = dict()

for idx in range(n):
    key = num_list[idx]
    if key in num_dict:
        num_dict[key].append(idx)
    else:
        num_dict[key] = [idx]

rlt = [ 0 for _ in range(n)]

min_num = min(num_list)
max_num = max(num_list) 

num_list = list(set(sorted(num_list)))
num_list.sort()

# print(num_list)
# print(num_dict)

cnt = 0
for idx in range(len(num_list)):
    
    for i in num_dict[num_list[idx]]:
        rlt[i] = cnt
    
    cnt += 1
    
print(*rlt)
