from collections import deque

N = int(input())

lst = list(map(int,input().split()))
ans = 0
def margesort(start, end):
    global ans
    if not(start < end):
        return [lst[start]]
    mid = (start+end)//2
    left = margesort(start,mid)
    right = margesort(mid+1,end)

    rlt = []

    _left = deque(left)
    _right = deque(right)
    while _left and _right:
        l_now = _left[0]
        r_now = _right[0]

        if l_now <= r_now:
            rlt.append(_left.popleft())
        else:
            rlt.append(_right.popleft())
            ans += len(_left)
        
    if _left:
        rlt += list(_left)
    if _right:
        rlt += list(_right)

    return rlt


margesort(0, N-1)
print(ans)