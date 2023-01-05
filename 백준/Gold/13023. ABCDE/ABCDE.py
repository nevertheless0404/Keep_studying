import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visit = [False] * n
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    # 친구 관계 넣기
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, f):
    global cnt
    # 시작 정점 방문
    visit[v] = True
    # 친구가 5명 다 연결되어 있으면
    if f == 5:
        cnt = 1
    else:
        for i in graph[v]:
            # 방문하지 않았다면 
            if not visit[i]:
                # 재귀적으로 수행
                dfs(i, f + 1)
                # 방문표시 해제
                visit[i] = False
                if cnt:
                    return


for j in range(n):
    # 친구 관계 탐색
    dfs(j, 1)
    # 현재 방문 표시 해제
    visit[j] = False
    # 친구 관계가 존재한다면 탈출!
    if cnt:
        break

print(cnt)