import sys
input = sys.stdin.readline

P = [0 for i in range(101)]
P[1] = 1
P[2] = 1
P[3] = 1 

for i in range(4, 101):
    P[i] = P[i - 3] + P[i - 2]
    
t = int(input())
for i in range(t):
    n = int(input())
    print(P[n])