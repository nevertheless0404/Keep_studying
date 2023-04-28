import sys 
input = sys.stdin.readline

MOD = 1000000007

n = 8
m = {}
d = int(input())

m[1] = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0],
]

def f(d, frm, t):
    if d <= 1:
        return m[d][frm][t]
    
    m.setdefault(d, [[0 for _ in range(n)] for _ in range(n)])
    if m[d][frm][t]:
        return m[d][frm][t]
    
    half = d // 2
    other = half + 1 if d % 2 else half # 홀수면 +1
    # half <= other

    for k in range(n):
        m[d][frm][t] += f(half, frm, k) * f(other, k, t)
        m[d][frm][t] %= MOD

    return m[d][frm][t]


print(f(d, 0, 0))