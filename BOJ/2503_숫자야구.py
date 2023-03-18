# https://www.acmicpc.net/problem/2503

import sys
from itertools import permutations

input = sys.stdin.readline

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3개씩 뽑기!
n = list(permutations(items, 3))
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    a = list(str(a))

    # 제거된 튜플 개수
    removed_cnt = 0

    l = len(n)
    for i in range(l):
        s_cnt = 0
        b_cnt = 0
        i -= removed_cnt

        for j in range(3):
            a[j] = int(a[j])
            if a[j] in n[i]:
                if j == n[i].index(a[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1

        if s_cnt != b or b_cnt != c:
            n.remove(n[i])
            removed_cnt += 1

print(len(n))
