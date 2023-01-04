n = int(input())
dp = [0] * (n + 1)

# 2부터 n까지 반복
for i in range(2, n + 1):
    # 2와 3으로 나누어 떨어지지 않는다면 무조건 1을 빼야함
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])