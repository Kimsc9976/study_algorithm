N = int(input())
dp = [0] + [0 for _ in range(N//2 + 4)]
dp[0] = 1
dp[1] = 3

if N %2 != 0:
    print(0)
else:
    n = N//2

    for i in range(2,n+1):
        dp[i] += dp[i-1]* 3 + 2
        for j in range(2,i):
            dp[i] += dp[i-j]*2
    print(dp[n])