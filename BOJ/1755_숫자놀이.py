# https://www.acmicpc.net/problem/1755

import sys

input = sys.stdin.readline
numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

m, n = map(int, input().split())

ans = []

for i in range(m, n + 1):
    if len(str(i)) == 1:
        ans.append(numbers[i])
    else:
        num = ""
        for j in str(i):
            num += numbers[int(j)] + " "
        num.rstrip()
        ans.append(num)
ans.sort()
answer = []

for i in ans:
    if " " in i:
        i = i.split(" ")
        num = ""
        for j in i:
            if j != "":
                num += str(numbers.index(j))
        num = int(num)
        answer.append(num)
    else:
        answer.append((numbers.index(i)))
for i in range((len(answer) // 10) + 1):
    print(*answer[i * 10 : i * 10 + 10])
