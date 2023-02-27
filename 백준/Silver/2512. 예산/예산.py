N = int(input())
pay = list(map(int,input().split()))
total = int(input())

if sum(pay) <= total:
    print(max(pay))
else:
    avg = total//N
    m = 0
    M = 0

    pay.sort()
    start = 0
    end = max(pay)
    while start <= end:
        mid = (start + end)//2
        curr = 0 # 예산 분배금 
        for tax in pay:
            if tax >= mid:
                curr += mid
            else:
                curr += tax
        if curr <= total:
            start = mid + 1
        else:
            end = mid - 1
    print(end)
