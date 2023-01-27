# https://www.acmicpc.net/problem/8979

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
medal = []

for i in range(n):
    m = list(map(int, input().split()))
    medal.append(m)

medal.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(n):
    # 등수를 알고 싶은 국가 넣기
    if medal[i][0] == k:
        rank = i

for i in range(n):
    if medal[rank][1:] == medal[i][1:]:
        print(i + 1)
        break
