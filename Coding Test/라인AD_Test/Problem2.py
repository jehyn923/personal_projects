import heapq
def solution(array):
    
    map = {}
    idx_map = {}
    bigger_idx =[]
    answer = []
    minimum_x = len(array)
    min_loc = 0

    #초기화 
    for i in range(len(array)):
        answer.append(0)
        biggerList = list(filter(lambda x: x>array[i],array))
        map[array[i]]=i
        idx_map[i] = array[i] 
  
        

    for i in range(len(array)):
        if array[i] == max(array):
            answer[i] = -1
        
        else:
            biggerList = list(filter(lambda x: x>array[i],array))
            min_loc = 0
            minimum_x = len(array)

            for j in range(len(biggerList)):
                print(biggerList)
                print(min_loc)
                if minimum_x > abs(i-map[biggerList[j]]):
                   min_loc = map[biggerList[j]]
                   minimum_x = abs(i-map[biggerList[j]])

                elif minimum_x ==  abs(i-map[biggerList[j]]):
                    if min_loc > map[biggerList[j]]:
                        min_loc = map[biggerList[j]]
                   
            answer[i] = min_loc
            #for j in ra   nge(len(biggerList)):
                
    
    print(answer)
    print(map)
    print(idx_map)


#최단거리문제


    return answer

solution([3,5,4,1,2])