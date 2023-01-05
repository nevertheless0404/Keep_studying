import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 서쪽에 1개 동쪽에 n개가 있을 때
            # n 개 지을 수 있음
            if i == 1:
                dp[i][j] = j
                continue
            # 서, 동쪽에 사이트 개수가 같으면 1개만 지을 수 있음
            if i == j:
                dp[i][j] = 1

            else:
                # 이항 계수
                # (j-1) 개 원소중에 i 원소만 뽑고 j 번째 원소 버리기
                # (j-1)개 원소중에 (i-1)개 원소를 뽑고 j 번째 원소로 포함
                if j > i:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
    print(dp[n][m])