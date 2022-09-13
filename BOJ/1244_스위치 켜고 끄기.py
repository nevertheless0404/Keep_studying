# https://www.acmicpc.net/problem/1244

import sys
sys.stdin = open("/Users/yuyeong/Desktop/KEEP STUDYING/BOJ/1244_스위치 켜고 끄기.txt")

num = int(input())
switch = list(map(int, input().split()))
# 학생수 
student = int(input())

for _ in range(student):
    s, n = map(int, input().split())
    # 남학생일 일때는 번호의 배수에 해당되는 스위치의 상태를 변경 
    if s == 1:
        # 숫자를 0부터 시작하게 해주기 
        for i in range(n-1, num, n):
            if switch[i]:
                switch[i] = 0
            else:
                switch[i] = 1

    else:
        n -= 1
        # left와 right에 해당되는 스위치의 상태가 같다면 상태를 변경
        left = right = n
        # 인덱스가 넘어가면 안됨
        while left >= 0 and right < num:
            if switch[left] == switch[right]:
                if switch[left]:
                    switch[left] = 0
                    switch[right] = 0
                else:
                    switch[left] = 1
                    switch[right] = 1
            else:
                break
            # 상태를 변경할 때마다 left는 -1 right +1
            left -= 1
            right += 1
# 20이하일 때는 그대로 출력 초과할 때는 20개씩 출력 
if num <= 20:
    print(*switch)
else:
    for i in range(len(switch)):
        print(switch[i], end= " ")
        if i+1 >= 20 and (i+1)%20 == 0:
            print()