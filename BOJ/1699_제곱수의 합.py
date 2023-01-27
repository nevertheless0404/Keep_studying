# https://www.acmicpc.net/problem/1699

import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = i

    for j in range(1, i):
        if (j * j) > i:
            break
        # 최소항의 개수가 아님!
        if dp[i] > dp[i - j * j] + 1:
            # 최소항의 개수를 바꿔줘야 함
            dp[i] = dp[i - j * j] + 1

print(dp[n])
