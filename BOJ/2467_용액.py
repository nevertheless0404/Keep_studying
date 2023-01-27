# https://www.acmicpc.net/problem/2467

import sys

input = sys.stdin.readline

value = 2000000000
n = int(input())
liquid = list(map(int, input().split()))

# 투 포인터
left, right = 0, n - 1
l_left, l_right = 0, 0

while left < right:
    tmp = liquid[left] + liquid[right]

    # 현재 두 용액의 합의 절대값이 value 보다 작을 경우
    if abs(tmp) < value:
        value = abs(tmp)
        l_left, l_right = liquid[left], liquid[right]

    if tmp == 0:
        break

    elif tmp < 0:
        left += 1

    else:
        right -= 1

print(l_left, l_right)
