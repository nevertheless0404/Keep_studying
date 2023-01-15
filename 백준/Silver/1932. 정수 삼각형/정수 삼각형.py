import sys

input = sys.stdin.readline

n = int(input())
floor = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        # 층 첫번째 값은 이전 층의 첫번째 위치의 값만 더 할 수 있음
        if j == 0:
            floor[i][j] += floor[i - 1][0]
        # 층 마지막 값은 이전 층의 마지막 위치의 값만 더 할 수 있음
        elif j == (i):
            floor[i][j] += floor[i - 1][-1]
        # 점화식에 따라 계산
        else:
            floor[i][j] += max(floor[i - 1][j - 1], floor[i - 1][j])

print(max(floor[-1]))