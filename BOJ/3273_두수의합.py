# https://www.acmicpc.net/problem/3273

import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
x = int(input())
num.sort()

ans = 0
left, right = 0, n - 1
while left < right:
    temp = num[left] + num[right]

    if temp == x:
        ans += 1
        left += 1
    # 두 수의 합이 x 보다 큰 경우 더 큰 값을 더해야 함
    elif temp < x:
        left += 1

    # 더 작은 값을 더해야 함
    else:
        right -= 1

print(ans)
