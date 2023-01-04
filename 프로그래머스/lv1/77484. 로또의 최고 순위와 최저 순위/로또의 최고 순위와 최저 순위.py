def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    # 0 의 개수를 찾아서 넣음
    # 최고 순위를 구할때 '0'이 모두 win_nums의 숫자 중 하나라고 생각하고 
    # 0의 개수를 구하고 일치하는 숫자의 개수를 더해줌 
    cnt = lottos.count(0)
    answer = 0
    for i in win_nums:
        if i in lottos:
            answer += 1
    return rank[cnt + answer], rank[answer]