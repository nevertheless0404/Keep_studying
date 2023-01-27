# https://www.acmicpc.net/problem/12865

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
list_n = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n)]

for i in range(n):
    w = list_n[i][0]
    v = list_n[i][1]

    for j in range(1, k + 1):
        # 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다.
        if j < w:
            dp[i][j] = dp[i - 1][j]

        else:
            # 넣을 물건의 무게만큼 배낭에서 빼고 현재 물건을 넣음
            # 물건을 넣지 않고 이전 배낭 그대로 가져감
            dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])

print(dp[-1][k])
