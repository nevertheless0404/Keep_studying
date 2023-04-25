import sys 
input = sys.stdin.readline

# dp[길이][마지막수][비트값]

mod = 1000000000
n = int(input())
dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(n + 1)]
for i in range(1, 10):
    dp[1][i][1 << i] = 1
    
for j in range(n):
    for k in range(10):
        for bit in range(1024):
            if k < 9:
                next_bit = bit | (1 << (k + 1))
                dp[(j + 1)][k + 1][next_bit] += dp[j][k][bit]
                dp[(j + 1)][k + 1][next_bit] %= mod
                
            if k > 0:
                next_bit = bit | (1 << (k - 1))
                dp[(j + 1)][k - 1][next_bit] += dp[j][k][bit]
                dp[(j + 1)][k - 1][next_bit] %= mod
                
result = 0
for l in range(10):
    result += dp[n][l][1023]
    result %= mod
    
print(result)