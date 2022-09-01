# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

from collections import deque
import sys
sys.stdin = open("/Users/yuyeong/Desktop/KEEP STUDYING/SW/5097_회전.txt")

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = deque(list(map(int, input().split())))

    for i in range(m):
        num = arr.popleft() # 맨 앞에 숫자를 삭제하고 반환
        arr.append(num) # 맨 뒤로 삽입
   
    print("#%d %d" % (tc, arr.popleft()))