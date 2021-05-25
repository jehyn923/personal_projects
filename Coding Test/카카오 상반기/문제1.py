def solution(s):
    answer = 0
    answer_str=''
    numbers = { 'one' : 1 ,'two':2, 'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    numb_alp =''
    for i in range(len(s)):
        if s[i].isalpha():
            numb_alp+=s[i]
            if numb_alp in numbers:
                answer_str+=str(numbers[numb_alp])
                numb_alp = ''
        else:
            
            answer_str+=str(s[i])

    answer=int(answer_str)
    return answer

solution("one4seveneight")
solution("23four5six7")
solution("2three45sixseven")
solution("123")