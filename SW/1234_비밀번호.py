# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14_DEKAJcCFAYD&

import sys
sys.stdin = open("/Users/yuyeong/Desktop/무제 폴더 2/sw/1234_비밀번호.txt")

for tc in range(1, 11):
    n, num = input().split()
    num = list(map(int,num))
    result = []

    for i in range(int(n)):
        # result에 숫자가 존재, 마지막 숫자와 현재 숫자가 같은 경우
        # 빼줘!!!!!
        # 아닌거면 넣어줘 
        if result and result[-1] == num[i]:
            result.pop()
            continue
        result.append(num[i])

    print('#%d %d'%(tc,int(''.join(map(str,result)))))

     
   
