import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
fruit_list = list(map(int, input().split()))

def max_fruits(fruits):
    count = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(fruits)):
        count[fruits[right]] += 1

        # 과일 종류가 3개 이상일 경우, 왼쪽 포인터 이동
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

print(max_fruits(fruit_list))
