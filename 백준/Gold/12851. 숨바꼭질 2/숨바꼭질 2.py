import sys

input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

visit = [[-1, 0] for _ in range(100001)]


def bfs(n):
    q = deque()
    q.append(n)
    # 시간
    visit[n][0] = 0
    # 경우의 수
    visit[n][1] = 1

    while q:
        postion = q.popleft()
        for i in (postion * 2, postion + 1, postion - 1):
            if 0 <= i < 100001:
                # 처음 방문하면 방문 처리 해줘
                if visit[i][0] == -1:
                    visit[i][0] = visit[postion][0] + 1
                    visit[i][1] = visit[postion][1]
                    q.append(i)
                    # 한번 이상 방문한 경우 방법 더하기
                elif visit[i][0] == visit[postion][0] + 1:
                    visit[i][1] += visit[postion][1]


bfs(n)
# 가장 빠른시간
print(visit[k][0])
# 방법의 수
print(visit[k][1])