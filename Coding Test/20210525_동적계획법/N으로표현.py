def solution(N, number):
    answer = 0
    N_set = [set() for i in range(8)]
    
    for i in range(len(N_set)):
        N_set[i].add(int(str(N)*(i+1)))
    
    for i in range(len(N_set)):
        for j in range(i):
            for el1 in N_set[j]:
                for el2 in N_set[i-j-1]:
                
                    N_set[i].add(el1 + el2)
                    
                    if el1 > el2:
                        N_set[i].add(el1 - el2)
                    if el1 != 0 and el2 != 0:
                        N_set[i].add(el1 * el2)
                        N_set[i].add(el1 // el2)
                        N_set[i].add(el2 // el1)

        if number in N_set[i]:
            answer = i + 1
            return answer
        else:
            answer = -1
    
    
    return answer