# https://www.acmicpc.net/problem/14501

n = int(input())

t = []
p = []
dp = [0 for _ in range(n + 1)]

for _ in range(n):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)

# 뒤에서부터
for i in range(n - 1, -1, -1):
    # 상당에 필요한 일수가 퇴사일을 넘긴다면?
    if t[i] + i > n:
        dp[i] = dp[i + 1]

    # 오늘 상담할 경우
    else:
        dp[i] = max(dp[i + 1], dp[t[i] + i] + p[i])

print(dp[0])
