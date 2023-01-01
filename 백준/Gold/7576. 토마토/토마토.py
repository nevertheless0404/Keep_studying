import sys 
from collections import deque 
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            # 익은 토마토 저장
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
                

            
bfs()
result = 0
for i in graph :
    for j in i :
        if j == 0 : 
            print(-1)
            exit(0)
    result = max(result,max(i))

print(result-1)
