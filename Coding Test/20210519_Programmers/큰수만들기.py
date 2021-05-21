def solution(number, k):
    answer = ''
    loc = 0
    new_arry_length = len(number)-k
    number_arry =[]
    return_arry = []
    number_arry.extend(number)

    while new_arry_length>0:
        
        

        return_arry.append(max(number_arry[:len(number_arry)-new_arry_length+1]))
        number_arry = number_arry[number_arry.index(return_arry[-1])+1:]
        
        new_arry_length -= 1

    answer = ''.join(return_arry)
    return answer


print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))