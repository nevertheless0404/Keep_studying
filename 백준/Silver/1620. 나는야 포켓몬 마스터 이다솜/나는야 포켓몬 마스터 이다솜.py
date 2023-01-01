# isdigit() 문자열이 숫자로만 구성되어있는지 판별

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
pokemon = {}

for i in range(n):
    data = input().rstrip()
    pokemon[i + 1] = data
    pokemon[data] = i + 1
    
for i in range(m):
    data = input().rstrip()
    if data.isdigit():
        print(pokemon[int(data)])
    else:
        print(pokemon[data])