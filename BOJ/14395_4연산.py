# https://www.acmicpc.net/problem/14395

import sys
from collections import deque

input = sys.stdin.readline

s, t = map(int, input().split())
# 순서가 정해져 있음
oper = ["*", "+", "-", "/"]


def bfs():
    q = deque()
    q.append((s, ""))
    visit = []

    while q:
        cnt = 0
        n, o = q.popleft()
        print(o)

        for i in oper:
            if i == "*":
                cnt = n * n
            elif i == "+":
                cnt = n + n
            elif i == "-":
                cnt = n - n
            # s 가 0이 아닐때만 사용 가능
            elif i == "/" and n != 0:
                cnt = int(n / n)


            if 0 < n <= 10**9:
                if cnt == t:
                    print(o + i)
                    return
                if cnt not in visit:
                    q.append((cnt, o + i))
                    visit.append(cnt)

    print(-1)
    return


if s == t:
    print(0)
else:
    bfs()
