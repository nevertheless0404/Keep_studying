import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
result = []

def dfs(N):
    if N == m:
        print(*result)
        return
    
    for i in range(n):
        if N == 0 or result[-1] <= data[i]:
            result.append(data[i])
            dfs(N + 1)
            result.pop()
dfs(0)
    