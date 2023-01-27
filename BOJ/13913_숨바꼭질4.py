# https://www.acmicpc.net/problem/13913

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
visit = [0] * 100001


def bfs(n):
    q = deque()
    q.append([n, 0, [n]])
    visit[n] = 1

    if n > K:
        # 도착하려면 뒤로가는 방법이 있고, n부터 K까지 1씩 감소!
        return n - K, [int(x) for x in range(n, K - 1, -1)]

    while q:
        x, cnt, road = q.popleft()

        if x == K:
            return cnt, road

        for i in [x - 1, x + 1, x * 2]:
            if 0 <= i <= 100000 and not visit[i]:
                visit[i] = 1
                r = road + [i]
                q.append([i, cnt + 1, r])


res_cnt, res_road = bfs(N)

print(res_cnt)
for j in res_road:
    print(j, end=" ")
