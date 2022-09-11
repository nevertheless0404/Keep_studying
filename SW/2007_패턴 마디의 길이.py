# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P1kNKAl8DFAUq&

from distutils.spawn import spawn
import sys
sys.stdin = open("/Users/yuyeong/Desktop/KEEP STUDYING/SW/2007_패턴 마디의 길이.txt")

t = int(input())
for tc in range(1, t+1):
    words = input()
    result = 0

    for i in range(1, len(words)):
        # 현재 확인하고 있는 문자가 0번째 문자와 같은지 확인
        if words[i] == words[0]:
            # 가장 첫 문자부터 i 번째 문자까지의 문자열과 i번쨰 문자부터 i*2번째 
            # 문자까지의 문자열이 같다면 할당
            if words[:i] == words[i:i*2]:
                result = i
                break
            # 문자열이 29일 경우 30을 할당한다.
            if i == 29:
                result = 30
        
    print('#%d %d' % (tc, result))