import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
visit = [0] * n
s = []

def dfs(start):
    if start == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(n):
        if not visit[i]:
            s.append(data[i])
            visit[i] = 1
            dfs(start + 1)
            visit[i] = 0
            s.pop()


dfs(0)