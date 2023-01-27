# https://www.acmicpc.net/problem/1931

import sys

input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

# 2차원 요소를 기준으로 정렬!
time.sort(key=lambda x: (x[1], x[0]))
print(time)

last_end = 0
cnt = 0

for start, end in time:
    if start >= last_end:
        print(last_end)
        last_end = end
        cnt += 1

print(cnt)
