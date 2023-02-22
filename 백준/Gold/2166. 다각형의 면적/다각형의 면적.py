import sys 
input = sys.stdin.readline

n = int(input())
poly = [list(map(int, input().split())) for _ in range(n)]
poly.append(poly[0])

sum = 0 

for i in range(n):
    sum += (poly[i][0] * poly[i + 1][1]) - (poly[i][1] * poly[i + 1][0])


print(round(abs(sum/2), 1))