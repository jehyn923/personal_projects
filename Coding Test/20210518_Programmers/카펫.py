def solution(brown, yellow):
    answer = []
    possibleAns = []

    for i in range(1, yellow+1):
        if yellow % i == 0:
            possibleAns.append(i)
    
    for i in range(len(possibleAns)):
        yWidth = yellow // possibleAns[i]
        yHeight = possibleAns[i]
        bWidth = yWidth+2
        bHeight = yHeight+2
        coverNum = (bWidth+bHeight)*2 - 4 
        if coverNum == brown:
            answer.append(bWidth)
            answer.append(bHeight) 
            return answer
    
    
    return answer

solution(10,2)
solution(8,1)
solution(24,24)