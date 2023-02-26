import sys 
input = sys.stdin.readline

n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1
    
for i in range(2, n + 1):
    # index
    for j in range(10):
        # 뒷자리가 0일 때는 1 밖에 못옴
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else :
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)