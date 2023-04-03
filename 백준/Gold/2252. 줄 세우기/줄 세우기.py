import sys 
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

q = deque()

for i in range(1, n + 1):
    if inDegree[i] == 0:
        q.append(i)

result = []

while q:
    i = q.popleft()
    result.append(i)

    for j in graph[i]:
        inDegree[j] -= 1
        if inDegree[j] == 0:
            q.append(j)

print(*result, sep=" ")
