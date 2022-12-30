import sys
input = sys.stdin.readline

k = int(input())
wrong = []

for i in range(k):
    num = int(input())
    if num == 0:
        wrong.pop()
    else:
        wrong.append(num)

print(sum(wrong))