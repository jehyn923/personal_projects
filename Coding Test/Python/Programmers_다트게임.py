import math

def solution(dartResult):
    answer = 0
    round = -1
    
    chance = dict()
            
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            #flag를 사용해서 10인거 체크하는 방법.
            #stack이나 queue를 이용해서 숫자 저장하기 생각(if, else문 덕지덕지라 바꾸고 싶음)
            if dartResult[i] =='1':
                if dartResult[i+1] =='0':
                    continue
                else:
                    round += 1
                    chance[round]=int(dartResult[i])
            elif dartResult[i] =='0':
                if dartResult[i-1] == '1':
                    round += 1
                    chance[round] = 10
                else:
                    round += 1
                    chance[round] = 0
            else:
                round += 1
                chance[round] = int(dartResult[i])
                
        elif dartResult[i].isalpha():
            if dartResult[i] == 'D':
                chance[round] = math.pow(chance[round],2)
            elif dartResult[i] == 'T':
                chance[round]  = math.pow(chance[round],3)

        else:
            if dartResult[i] =='*':
                chance[round] *= 2
                if round>0:
                    chance[round-1] *=2
                    
            elif dartResult[i] == '#':
                chance[round] *= -1  
                    
            
    
    for i in range(len(chance)):
        answer += chance[i]
    
    return answer