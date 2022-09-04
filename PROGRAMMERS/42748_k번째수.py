# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        arr_list = array[commands[i][0]-1:commands[i][1]]
        arr_list.sort()
        
        answer.append(arr_list[commands[i][2]-1])
    return answer