import sys
input = sys.stdin.readline

k = int(input().rstrip())
str = input().rstrip()

arr = []
str_1 = ''

for i in range(int(len(str)/k)):
    if i % 2 == 1:
        str_1 = str[i*k:i*k+k]
        arr.append(str_1[::-1])
    else:
        arr.append(str[i*k:i*k+k])
        
for i in range(k):
    for j in range(int(len(str)/k)):
        print(arr[j][i], end = "")