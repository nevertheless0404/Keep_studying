# https://www.acmicpc.net/problem/2011

import sys

input = sys.stdin.readline

code = list(map(int, input().rstrip()))
l = len(code)

# i 번째 수 단계에서 암호 코드의 개수
dp = [0] * (l + 1)

# 암호가 잘못되어 암호 해석을 할 수 없는 경우
if code[0] == 0:
    print(0)

else:
    code = [0] + code
    dp[0] = 1
    dp[1] = 1

    for i in range(2, l + 1):
        # 한 자리수
        cipher = code[i]
        # 두 자리수
        cipher_2 = code[i - 1] * 10 + code[i]

        if cipher >= 1 and cipher <= 9:
            dp[i] += dp[i - 1]

        if cipher_2 >= 10 and cipher_2 <= 26:
            dp[i] += dp[i - 2]

        dp[i] %= 1000000

    print(dp[l])
