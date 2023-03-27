n = int(input())

for i in range(n):
    cnt, word = input().split()
    text = ''
    for i in word:
        text += int(cnt) * i
    print(text)
        