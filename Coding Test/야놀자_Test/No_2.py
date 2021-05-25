def solution (S):
    
    N = len(S)     
    answer = set()
    

    for i in range(N):
        num_s = [S[i] for i in range(N)]
        for j in range(10):
            #print(num_s)
            num_s[-(i+1)] = str(j)          
            num = int(''.join(num_s))
            if num%3 == 0:
                answer.update([num])
                #print(num)
                #answer.append(num)
                #num += 3*10**i #digit만큼 더 해주기
        
        
#X,Y,Z
    

    print(len(answer))
    #print(answer)

solution("23")
solution("0081")
solution("022")

