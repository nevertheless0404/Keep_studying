import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
broken = list(map(str, sys.stdin.readline().split()))
cnt = abs(100 - n) # 리모컨을 눌러야하는 최대 개수

# 반복문을 통해 이동해야하는 채널로 가기 위한 방법을 확인
for i in range(1000001):

    # 반복문을 통해 채널로 이동하기 위해 눌러야 하는 번호가 고장이 났는지 확인
    for j in str(i):
        if j in broken:
            break

    # 채널로 이동 가능하다면 원래 cnt와 채널을 누른 개수와 +/- 를 누른 개수를 cnt에 담는다.
    else:
        cnt = min(cnt, len(str(i)) + abs(i - n))

print(cnt)
    