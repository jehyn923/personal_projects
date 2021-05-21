def solution(answers):
    supoAnswer = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    correctMax = 0
    answer = []

    for i in range(len(supoAnswer)):
        correctAnswer = 0
        for j in range(len(answers)):
            if supoAnswer[i][j%len(supoAnswer[i])] == answers[j]:
                correctAnswer += 1
                
        if correctMax < correctAnswer:
            if answer:
                answer.pop()
            answer.append(i+1)
            correctMax = correctAnswer
        elif correctMax == correctAnswer:
            answer.append(i+1)

    answer.sort()
    
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))