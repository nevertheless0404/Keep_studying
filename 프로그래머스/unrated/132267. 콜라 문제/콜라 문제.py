def solution(a, b, n):
    answer = 0
    # 빈 병의 개수 n이 교환 가능한 최소 숫자 a 이상일때 계속 반복
    while n >= a:
        # 현재 빈 병으로 받을 수 있는 새로운 개수 및 나머지 계산
        newcnt = n // a * b
        leftcnt = n % a
        
        # 빈 병 개수
        answer += newcnt
        n = newcnt + leftcnt       
    return answer