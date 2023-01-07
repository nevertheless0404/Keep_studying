def solution(food):
    answer = '0'
    
    # 칼로리가 큰 음식부터 문자열 오른쪽과 왼쪽에 추가 
    for i in range(len(food)-1, 0, -1):
        answer = str(i)*(food[i]//2)+answer
        answer = answer+str(i)*(food[i]//2)
    return answer