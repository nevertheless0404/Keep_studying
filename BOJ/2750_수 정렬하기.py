# https://www.acmicpc.net/problem/2750

n = int(input())
a = [0]*n

for i in range(n):
    a[i] = int(input())

for i in range(n-1):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1] = temp
for i in range(n):
    print(a[i])


# n = int(input())
# a = []

# for i in range(n):
#     a.append(int(input()))

# a.sort()

# for j in range(n):
#     print(j)