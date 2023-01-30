import sys
from heapq import heappush, heappop

input = sys.stdin.readline

INF = sys.maxsize

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 1


def bfs():
    q = []
    heappush(q, (graph[0][0], 0, 0))
    visit[0][0] = 0

    while q:
        link, x, y = heappop(q)

        if x == (n - 1) and y == (n - 1):
            print(f"Problem {cnt}: {visit[x][y]}")
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            else:
                nc = link + graph[nx][ny]

                if nc < visit[nx][ny]:
                    visit[nx][ny] = nc
                    heappush(q, (nc, nx, ny))


while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    visit = [[INF] * n for _ in range(n)]
    bfs()
    cnt += 1