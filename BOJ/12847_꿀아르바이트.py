# https://www.acmicpc.net/problem/12847

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
number = list(map(int, input().split()))

step = m
window = sum(number[:step])
answer = window

for i in range(step, n):
    window += number[i] - number[i - step]

    answer = max(answer, window)
print(answer)
