import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
M = len(str(N))


def bfs(N, K):
    visit = set()
    visit.add((N, 0))
    q = deque()
    q.append((N, 0))
    result = 0

    while q:
        n, k = q.popleft()
        if k == K:
            result = max(result, n)
            continue
        n = list(str(n))
        for i in range(M - 1):
            for j in range(i + 1, M):
                if i == 0 and n[j] == "0":
                    continue
                # i번 위치의 숫자와 j번 위치의 숫자를 바꾼다
                n[i], n[j] = n[j], n[i]
                nn = int("".join(n))

                if (nn, k + 1) not in visit:
                    q.append((nn, k + 1))
                    visit.add((nn, k + 1))
                n[i], n[j] = n[j], n[i]

    # answer가 0이 아니라면 answer, else -1 리턴
    return result if result else -1


print(bfs(N, K))