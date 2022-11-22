# https://school.programmers.co.kr/learn/courses/30/lessons/12926


def solution(s, n):
    s = list(s)

    for i in range(len(s)):
        if s[i].isupper():
            # 문자열의 아스키코드에서 A/a의 아스키 값을 뺀 후 n을 더해서 문자열이 몇번째 알파벳인지 파악
            s[i] = chr((ord(s[i]) - ord("A") + n) % 26 + ord("A"))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord("a") + n) % 26 + ord("a"))
        else:
            continue

    return "".join(s)
