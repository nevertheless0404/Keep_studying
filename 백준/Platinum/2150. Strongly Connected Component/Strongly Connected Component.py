import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e= map(int, input().split())
graph = [[] for _ in range(v + 1)]
reverse_g = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    reverse_g[b].append(a)
    
    
def dfs(node, visit, stack):
    visit[node] = 1
    for k in graph[node]:
        if visit[k] == 0:
            dfs(k, visit, stack)
    stack.append(node)
    
def reverse_dfs(node, visit, stack):
    visit[node] = 1
    stack.append(node)
    for k in reverse_g[node]:
        if visit[k] == 0:
            reverse_dfs(k, visit, stack)
           
stack = []
visit = [0] * (v + 1)

for i in range(1, v + 1):
    if visit[i] == 0:
        dfs(i, visit, stack)
visit = [0] * (v + 1)
result = []

while stack:
    ssc = []
    node = stack.pop()
    if visit[node] == 0:
        reverse_dfs(node, visit, ssc)
        result.append(sorted(ssc))
        
print(len(result))
re = sorted(result)
for i in re:
    print(*i, -1)
        