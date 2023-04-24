import sys 
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

q = []
for i in range(1, n + 1):
    if in_degree[i] == 0:
        heapq.heappush(q, i)
        
result = []
while q:
    i = heapq.heappop(q)
    result.append(i)
    
    for j in graph[i]:
        in_degree[j] -= 1
        if in_degree[j] == 0:
            heapq.heappush(q, j
                          )
                
print(' '.join(map(str, result)))