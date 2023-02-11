import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

# 처음부터 탐색
for i in range(1, n):
    # 처음의 수와 비교할 값들 탐색
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

result = max(dp)
list = []

for i in range(n - 1, -1, -1):
    if dp[i] == result:
        list.append(a[i])
        result -= 1

list.reverse()
for i in list:
    print(i, end=" ")