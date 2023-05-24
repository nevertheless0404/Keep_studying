import sys 
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
    
dp = [[0, 1] for _ in range(n)]
visit = [False for _ in range(n)]

def dfs(node):
    for m in graph[node]:
        if not visit[m - 1]:
            visit[m - 1] = True
            dfs(m)
            # 0은 얼리어답터가 아님, 1은 얼리어답터 
            dp[node - 1][0] += dp[m - 1][1]
            dp[node - 1][1] += min(dp[m - 1])
            
visit[0] = True
dfs(1)
print(min(dp[0]))