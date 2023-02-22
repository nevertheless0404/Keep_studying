import sys 
input = sys.stdin.readline

# n = 20, k = 5
# 20을 5로 나눈 것은[0 + (20을 4개로 나눈것)] + [1 + (19를 4개로 나눈것)
# 점화식 이용 
n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(0, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[n][k] % 1000000000)