import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

s = input()
l = len(s)

dp = [2500 for _ in range(l + 1)]
dp[-1] = 0
p = [[0 for _ in range(l)] for _ in range(l)]

for i in range(l):
    p[i][i] = 1
    
for i in range(1, l):
    if s[i - 1] == s[i]:
        p [i - 1][i] = 1
        
for j in range(3, l + 1):
    for k in range(l - j + 1):
        e = k + j - 1
        if s[k] == s[e] and p[k + 1][e - 1]:
            p[k][e] = 1
            
for e in range(l):
    for k in range(e + 1):
        if p[k][e]:
            dp[e] = min(dp[e], dp[k - 1] + 1)
        else:
            dp[e] = min(dp[e], dp[e - 1] + 1)
            
print(dp[l - 1])