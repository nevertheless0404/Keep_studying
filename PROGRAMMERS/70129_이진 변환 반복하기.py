# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    # 이진 변환 횟수, 제거된 0의 개수
    answer = []
    cnt = 0
    num = 0
    while s != '1':
        # 모든 0 제거
        num += s.count('0')
        # 모든 1 제거
        len_num = s.count('1')
        # 진법  변환
        s = bin(len_num)[2:]
        cnt +=1

    answer.append(num)
    answer.append(cnt)
    return answer




