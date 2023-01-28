# https://www.acmicpc.net/problem/1068

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def dfs(delete):
    # 지워야 하는 노드와 해당 노드가 부모 노드인 자식노드의
    # 값을 모두 변환
    tree[delete] = -2

    for i in range(n):
        if delete == tree[i]:
            dfs(i)


n = int(input())
tree = list(map(int, input().split()))
d = int(input())
cnt = 0

# 노드 삭제
dfs(d)

# 부모 배열 탐색(-2), 해당 노드를 부모로 하는 노드가 부모 배열에 없을 경우
# +1
for i in range(n):
    if tree[i] != -2 and i not in tree:
        cnt += 1

print(cnt)
