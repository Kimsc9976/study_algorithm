N = int(input())
nums = list(map(int, input().split()))
index = [-1] * (N + 1)

for idx, value in enumerate(nums):
    index[value] = idx # 각 번호가 현재 nums 배열에서 어디에 존재하는지 기록

longest = 0
cnt = 1

for i in range(1, N):
    if index[i] < index[i + 1]: # 번호 i가 nums 배열 내에서 번호 i + 1보다 앞에 존재한다면
        cnt += 1 # 오름차순의 길이가 1 증가했음을 기록
    else:
        cnt = 1
    longest = max(longest, cnt) # 지금까지 기록한 최장 길이를 갱신

# 번호 배열의 전체 길이에서 1씩 차이나는 가장 긴 오름차순의 길이를 제거
print(N - longest if N != 1 else 0) # N = 1이면 움직일 필요가 없다.
            
'''
좀 어지럽긴 한데, 정리를 해보겠다. 문제의 예시를 보면
문제의 핵심은 오름차순이 되어버린 정렬은 옮길 필요가 없다는 것이다
먼저 간단한 예시를 살펴보자.
2
1 2와

2 
2 1의 경우를 살펴보자면

각각
[-1, 0, 1] 
[-1, 1, 0]이다.

1번 케이스는 1번과 2번이 정 방향으로 있기 때문에 움직일 필요가 없다.
카운팅했던 가장 긴 오름차순은 1(기본) + 1 이며
총 갯수의 2 - 2 = 0

2번 케이스는 2번과 1번이 역방향으로 있기 때문에 움직여야한다.
카운팅했던 가장 긴 오름차순은 1(기본) + 0 이며
이동시킬 횟수는 2, 혹은 1을 한번 옮긴
총 갯수의 2 - 1 


이제 
5
5 2 4 1 3
를 보자

이런식으로 나와있다.
index 리스트는 
[-1, 3, 1, 4, 2, 0] 로 리스트 업 될 것이다. ([ 0, 1, 2, 3, 4, 5]의 위치에 대한 정보를 기록)

2번이 3번보다 앞에 있기 때문에 이동이 필요없다
즉 카운팅 되는 가장 긴 오름차순은 1(기본) + 1

오름차순 된 것을 제외하고 하나씩 이동

총 갯수 5 - 2 = 3

한 예제를 더 들어보겠다.
7
3 5 2 6 1 7 4

이동 시킬 횟수는
4를 맨 앞으로
3을 맨 앞으로
2를 맨 앞으로
1을 맨앞으로
4회가 될 것이다.

이게 어떻게 되냐면,
index 리스트는 
[-1, 4, 2, 0, 6, 1, 3, 5] 로 리스트 업 될 것이다. 
일단 3은 4보다 앞에있다.
즉 카운팅 되는 가장 긴 오름차순은 1(기본) + 1 = 2
그런데 4(6번째)가 5(첫번째)보다 뒤에 있기 때문에 이건 다시 고려해보아야한다.
cnt 를 1로 바꾼다.

그다음은 다시 반복이다 1+1+1 = 3 이 나오고, 이게 가장 큰 오름차순이다.
이후 총 갯수 7 - 3 = 4 가 나온다.
'''   