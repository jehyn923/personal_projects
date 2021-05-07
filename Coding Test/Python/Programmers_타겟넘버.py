def solution(numbers, target):
    answer = 0

    root =[0]
    for i in numbers:
        child = []

        for j in root:
            child.append(j+i)
            child.append(j-i)
        root = child
    
    
    answer=root.count(target)
    return answer

solution([1,1,1,1,1],3)