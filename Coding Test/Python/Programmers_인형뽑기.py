def solution(board, moves):
    answer = 0
    #각 행 stack 화
    gameStack = [[] for i in range(len(board))]
    basketStack = []
    vanished =[]
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                continue
            gameStack[j].append(board[i][j])
    
    print(gameStack)
    for i in range(len(moves)):
        
        if gameStack[moves[i]-1]:
            popDoll=gameStack[moves[i]-1].pop(0) 

            if basketStack:
                if basketStack[-1] == popDoll:                
                    vanished.append(basketStack.pop())
                    vanished.append(popDoll)
                    continue
        
        basketStack.append(popDoll)
        
    answer=len(vanished)
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
#4 3 1 1 3 2 empty 4