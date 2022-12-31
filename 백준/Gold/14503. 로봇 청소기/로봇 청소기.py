n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 시작지 방문 체크 
visited[r][c] = 1
cnt = 1

while True:
    # 아직 청소 안했음!
    flag = 0           
    for _ in range(4): 
        # 왼쪽 방향으로 한칸 돌림!!!
        d = (d + 3) % 4   
        nr = r + dr[d]
        nc = c + dc[d]

        # 범위 안에 들고, 빈칸이면 청소 할 수 있으면 
        # 들려서 청소하고, 카운트!
        # 현재위치 갱신, flag 변경 및 청소 
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                r = nr
                c = nc
                flag = 1        
                break
   
    if flag == 0:
        # 네 방향 모두 청소를 할 수 없을 때 
        # 후친 했을 때 벽이면 break
        # 만약 뒤가 벽이 아니라면!
        # 그 위치를 다시 갱신!!
        if arr[r-dr[d]][c-dc[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-dr[d], c-dc[d]