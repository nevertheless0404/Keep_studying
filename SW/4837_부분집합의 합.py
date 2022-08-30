# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open("/Users/yuyeong/Desktop/KEEP STUDYING/SW/4837_부분집합의 합.txt")

t = int(input())
for tc in range(1, t+1):
    N, K = map(int, input().split())

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(arr)
    total = []
    count = 0

    for i in range(1 << n):  # 1<<n:부분 집합의 개수
        sum_list = []
        for j in range(n):  # 원소의 수만큼 비트를 비교함
            if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
                sum_list.append(arr[j])
        total.append(sum_list)

    for i in range(len(total)):
        if len(total[i]) == N:

            sum_total = 0
            for l in range(len(total[i])):
                sum_total += total[i][l]
            if sum_total == K:
                count += 1

    print('#{} {}'.format(tc,count))
