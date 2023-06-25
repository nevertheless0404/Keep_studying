m = int(input())
n = int(input())

s_list = []
for i in range(m, n+1):
    count = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                count += 1
                break
                
        if count == 0:
            s_list.append(i)
            
            
if len(s_list) > 0:
    print(sum(s_list))
    print(min(s_list))
    
else:
    print(-1)