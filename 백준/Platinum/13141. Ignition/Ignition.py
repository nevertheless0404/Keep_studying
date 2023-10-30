import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[1e9] * n for _ in range(n)]
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    dp[a - 1][b - 1] = dp[b - 1][a - 1] = min(dp[a - 1][b - 1], c)
    graph.append((a - 1, b - 1, c))
    

# 플로이드 
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            
for i in range(n):
    dp[i][i] = 0 
result = 1e9

for i in range(n):
    MAX = 0
    for a, b, c in graph:
        MAX = max(MAX, (dp[i][a] + c + dp[b][i])/2)
    result = min(result, MAX)

print(result)




    
    
