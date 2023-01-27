# https://www.acmicpc.net/problem/2579

n = int(input())
# 계단 리스트
s = [int(input()) for _ in range(n)]

dp = [0] * (n)
# 계단이 2개 이하면 다 더함
if len(s) <= 2:
    print(sum(s))
# 계단이 3개 이상일 때 
else:
    # 첫번째 계단
    dp[0] = s[0]
    # 두번째 계단
    dp[1] = s[0]+s[1]
    for i in range(2, n):
        # 3번째 계단부터 2계단을 연속으로 걸었을 때, 1계단을 건너뛴 것을 비교해서 
        # 최댓값을 계속 갱신시켜나가는 것 
        dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])
    print(dp[-1])