import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

count = 0  # 현재까지 'OI'가 몇 번 반복됐는지
result = 0  # 결과: 몇 개의 Pn 패턴을 찾았는지
i = 0

while i < m - 1:
    if s[i] == 'I' and s[i + 1] == 'O':
        count = 0
        while i + 2 < m and s[i + 1] == 'O' and s[i + 2] == 'I':
            count += 1
            i += 2  # 'OI' 단위로 건너뜀
            if count == n:
                result += 1
                count -= 1  # 중첩 고려
        i += 1
    else:
        i += 1

print(result)