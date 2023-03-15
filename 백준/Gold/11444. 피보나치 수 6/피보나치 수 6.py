import sys 
input = sys.stdin.readline

n = int(input())
matrix = [[1, 1], [1, 0]]

def mul(a, b):
    res = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += a[i][k] * b[k][j] % 1000000007

    return res

def power(c, d):
    if d == 1:
        return c
    else:
        tmp = power(c, d // 2)
        # 짝수인 경우 
        if d % 2 == 0:
            return mul(tmp, tmp)
        else:
            return mul(mul(tmp, tmp), c)

result = power(matrix, n)

print(result[0][1] % 1000000007)