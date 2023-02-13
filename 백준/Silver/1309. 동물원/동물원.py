import sys 
input = sys.stdin.readline 

n = int(input())
dp = [[0] * 3 for _ in range(n + 1)]

for i in range(3):
    dp[1][i] = 1
    
for i in range(2, n + 1):
    # 오른쪽 사자 
    dp[i][0] = dp[i - 1][1] % 9901 + dp[i - 1][2] % 9901
    # 왼쪽 사자 
    dp[i][1] = dp[i - 1][0] % 9901 + dp[i - 1][2] % 9901
    # 둘 다 아님
    dp[i][2] = dp[i - 1][0] % 9901 + dp[i - 1][1] % 9901 + dp[i - 1][2] % 9901
    
print(sum(dp[n]) % 9901)