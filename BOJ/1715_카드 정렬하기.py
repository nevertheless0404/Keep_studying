# https://www.acmicpc.net/problem/1715

import heapq
n = int(input())

card = []
for _ in range(n):
    heapq.heappush(card, int(input()))
ans = 0

while len(card) != 1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)

    hao = first + second
    ans += hao
    heapq.heappush(card, hao)
print(ans)