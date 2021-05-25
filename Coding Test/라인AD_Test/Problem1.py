def solution(inputString):
    answer = 0
    open_parent = {'(':1,'{':2,'[':3,'<':4 } 
    close_parent = {')':1,'}':2,']':3,'>':4 } 
    used_parent = []
    count_parent = 0
    parent = False
    for i in range(len(inputString)):
        if inputString[i] in open_parent:
            parent = True
            count_parent += 1
            used_parent.append(inputString[i])
        if inputString[i] in close_parent:
            #사용된 괄호가 없을 때
            if not used_parent:
                if i < 1:
                    return 0
                else:
                    return answer
            tmp = used_parent.pop()
            if close_parent[inputString[i]] == open_parent[tmp]:
                continue

            else:
                answer = - i
                return answer
    if used_parent:
        answer = -(len(inputString)-1)
        return answer 

    if parent == True:
        return count_parent
    else: 
        return answer


print(solution("Hello, world!"))
print(solution("line [({<plus>)}]"))
print(solution("line [({<plus>})"))
print(solution(">_<"))
print(solution("x * (y + z) ^ 2 = ?"))