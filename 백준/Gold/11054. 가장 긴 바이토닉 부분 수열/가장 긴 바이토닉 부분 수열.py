import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp1 = [1] * n
dp2 = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp1[i] <= dp1[j]:
            dp1[i] = dp1[j] + 1

for i in range(n - 1, -1, -1):
    for j in range(i, n):
        if a[i] > a[j] and dp2[i] <= dp2[j]:
            dp2[i] = dp2[j] + 1
        
for i in range(n):
    dp1[i] = dp1[i] + dp2[i] - 1

print(max(dp1))