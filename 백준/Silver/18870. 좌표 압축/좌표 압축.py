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