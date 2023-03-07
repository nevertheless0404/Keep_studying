import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(x):
    global result
    visit[x] = True
    cycle.append(x)
    num = arr[x]

    if visit[num]:
        if num in cycle:
            result += cycle[cycle.index(num):]
        return
    
    else:
        dfs(num)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visit = [0] * (n + 1)
    result = []

    for i in range(1, n + 1):
        if not visit[i]:
            cycle = []
            dfs(i)

    print(n - len(result))