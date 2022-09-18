# https://www.acmicpc.net/problem/17413

import sys
sys.stdin = open("/Users/yuyeong/Desktop/KEEP STUDYING/BOJ/17413_단어 뒤집기2.txt")


s = list(input())
s.append(' ')
s_word = []
tag = False
for i in s :
    # '<'이나 공백 문자를 인식하면 있는 모든 문자를 탑부터 출력
    if i == '<':
        while s_word:
            print(s_word.pop(), end='')
        tag = True
        print('<',end ='')
    elif i == '>':
        tag = False
        print('>', end='')
    elif i == '':
        if tag: print('',end = '')
        else:
            while s_word:
                print(s_word,end='')
            print('',end='')
    else:
        if tag: print(i, end='')
        else: s_word.append(i)