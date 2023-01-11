def solution(my_string, num1, num2):
    answer = ''
    my_list = list(my_string)
    my_list[num1],my_list[num2] = my_list[num2],my_list[num1]
    return answer.join(my_list)