# 오일러 피 함수 
#  anwer * (1 - 1/p1) * (1 - 1/p2) * ..... * (1-1/pm)
#= (answer - answer / p1) * (1 - 1/p2) * ..... * (1-1/pm)

import sys 
input = sys.stdin.readline

n = int(input())
result = n

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        while n % i == 0:
            n //= i
            
        result -= result / i
        
if n > 1:
    result -= result / n 
    
print(int(result))