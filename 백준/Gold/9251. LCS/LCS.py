import sys
input = sys.stdin.readline

a = input().strip().upper()
b = input().strip().upper()

lcs = [[0] * (len(a) + 1) for _ in range(len(b) + 1)]

for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        if b[i - 1] == a[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

print(lcs[-1][-1])