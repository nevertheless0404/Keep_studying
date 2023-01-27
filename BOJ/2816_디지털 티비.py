# https://www.acmicpc.net/problem/2816

import sys

input = sys.stdin.readline

n = int(input())
channel = [input().rstrip() for _ in range(n)]

kbs1, kbs2 = channel.index("KBS1"), channel.index("KBS2")

# kbs1을 먼저 이동한 후에 kbs2를 이동
# kbs1이 뒤에 있다면 이동시키면서 kbs2 순서가 뒤로 감
if kbs1 > kbs2:
    kbs2 += 1


# kbs1이 있는 채널로 이동 (KBS1의 위치만큼 버튼 1 누름)
# kbs1을 첫 번째 순서로 이동시킴 (KBS1의 위치만큼 버튼 4 누름)
# kbs2가 있는 채널로 이동 (KBS2의 위치만큼 버튼 1 누름)
# kbs2를 두 번째 순서로 이동시킴 ((kbs2의 위치+1)만큼 버튼 4 누름(두 번째 위치이므로))
print("1" * kbs1 + "4" * kbs1 + "1" * kbs2 + "4" * (kbs2 - 1))
