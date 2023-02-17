import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tmp = list(map(int, input().split()))
tmp.sort()
lst = []
cnt = 0
visit = [0] * n


def dfs(start):
    cnt = 0
    if start == m:
        print(" ".join(map(str, lst)))
        return
    for i in range(n):
        if tmp[i] != cnt and visit[i] == 0:
            lst.append(tmp[i])
            cnt = tmp[i]
            visit[i] = 1
            dfs(start + 1)
            lst.pop()
            visit[i] = 0


dfs(0)