N,C = map(int,input().split())


arr = [int(input()) for _ in range(N)]
arr.sort()
is_travel = [False for _ in range(N)]


start = 1
end = arr[N - 1]
length = end - arr[0]

if C == 2:
    print(length)
else:
    ans = length
    end = length //(C-1)
    while start <= end:
        mid = (start + end) // 2 ## 왜 사람들이 거리차이를 start하고 end로 뒀을까
        curr = arr[0]
        count = 1

        for i in range(N):
            if (arr[i] - curr) >= mid:
                count += 1
                curr = arr[i]

        if count >= C:
            start = mid + 1
            ans = mid
        else: # count < C
            end = mid - 1
    print(ans)