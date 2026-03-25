import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    sticker = [ list(map(int, input().split())) for _ in range(2)]
    
    # print(sticker)
    ans = [[0 for _ in range(N)] for _ in range(2)]
    
    ans[0][0] = sticker[0][0]
    ans[1][0] = sticker[1][0]
    
    if N == 1:
        print(max(ans[0][0], ans[1][0]))
        continue

    ans[0][1] = sticker[1][0] + sticker[0][1]
    ans[1][1] = sticker[0][0] + sticker[1][1]
    if N == 2:
        print(max(ans[0][1], ans[1][1]))
        continue
    
    for i in range(2, N):
        ans[0][i] = max(ans[1][i - 2], ans[1][i - 1]) + sticker[0][i]
        ans[1][i] = max(ans[0][i - 2], ans[0][i - 1]) + sticker[1][i]

    print(max(ans[0][-1], ans[1][-1]))