import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)

def dfs (x, y):
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]

    land[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        # 지도 밖을 나가지 않게
        if 0 <= nx < h and 0 <= ny < w and land[nx][ny] == 1:
            dfs(nx, ny)
    
while True:
    w, h = map(int, input().split())
    # 바다이면 나와!
    if w == 0 and h == 0:
        break
    land = []
    count = 0
    for _ in range(h):
        land.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            # 땅이 있으면 증가!
            if land[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)
