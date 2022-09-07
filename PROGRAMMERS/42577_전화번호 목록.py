# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    phone_book.sort()
    # 거꾸로 탐색해주기
    for i in range(len(phone_book)-1):
        # 안에 있으면 False 그리고 멈춰
        if phone_book[i] in phone_book[1+i]:
            answer = False
            break
    return answer