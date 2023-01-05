n = int(input())

f = []
# 0과 1을 저장
f.append(0)
f.append(1)

for i in range(2, n+1):
    f.append(f[i-1]+f[i-2])
    
print(f[n])