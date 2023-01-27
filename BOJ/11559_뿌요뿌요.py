# https://www.acmicpc.net/problem/11559

import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 아래로 떨어지기 다른 뿌요가 있거나 바닥에 닿을때까지 뿌요를 떨어뜨린다.
def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if data[j][i] != "." and data[k][i] == ".":
                    print(j, i, k)
                    data[k][i] = data[j][i]
                    data[j][i] = "."
                    break

def bfs(a, b):
    q = deque()
    q.append((a, b))
    temp.append((a, b))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and data[nx][ny] == data[a][b] and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx, ny))
                temp.append((nx, ny))

data = [list(input().rstrip()) for _ in range(12)]
result = 0
while True:
    # 뿌요가 4개 이상 뭉쳤는지 확인
    flag = 0
    visit = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if data[i][j] != "." and not visit[i][j]:
                visit[i][j] = 1
                temp = []
                bfs(i, j)
                # 4칸인지 확인하고 뿌요가 뭉쳤으면 삭제!
                if len(temp) > 3:
                    flag = 1
                    for x, y in temp:
                        data[x][y] = "."

    # 뿌요가 없으면 더 이상 사라질 뿌요가 없어서 나와줘!
    if not flag:
        break
    # 삭제 한자리에 뿌요들을 내려주면 1 연쇄 추가!
    down()
    result += 1

print(result)
