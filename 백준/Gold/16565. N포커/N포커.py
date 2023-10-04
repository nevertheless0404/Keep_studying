import sys
input = sys.stdin.readline
from math import comb

mod = 10007
n = int(input())
result = 0

for i in range(1, n//4 + 1):
    val = (comb(13, i)*comb(52-(4 * i), n-(4 * i)))
    if i % 2:
        result += val % mod
    else:
        result -= val % mod


print(result % mod)