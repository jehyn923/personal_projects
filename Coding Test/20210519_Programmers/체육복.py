def solution(n, lost, reserve):
    answer = 0
    
    students = [0 for i in range(n)]

    for i in range(len(lost)):
        #잃어버린 학생 => lost[i]
        students[lost[i]-1] -= 1
    
    for i in range(len(reserve)):
        #여분이 있는 학생 reserve[i]
        students[reserve[i]-1] += 1
        

    for i in range(len(students)):
        if students[i] == -1:

            if i!= 0 and students[i-1] == 1:
                students[i] += 1
                students[i-1] -= 1
            elif i!=n-1 and students[i+1] == 1:
                students[i] += 1
                students[i+1] -= 1

    for i in range(len(students)):
        if students[i] >= 0:
            answer+=1
        
    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
