import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001

# 1, 2 값을 먼저 넣어줌 
dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    dp[i] = dp[i - 2] + dp[i - 1]

    # 방법의 수 나누기
print(dp[n] % 10007)

