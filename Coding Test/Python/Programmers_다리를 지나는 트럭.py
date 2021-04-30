def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    passing_queue = []
    passing_time_queue = []
    passed = []
    total = len(truck_weights)

    while len(passed)<total:
         #턴 종료, 시간 지나게 하기
        answer+=1

        for i in range(len(passing_time_queue)):
            #print(i)
            passing_time_queue[i]+=1
         
        
        #다리 건너고 있는 트럭 유무 체크
        if passing_queue:
            if passing_time_queue[0] >= bridge_length:
                passing_time_queue.pop(0)
                passed.append(passing_queue.pop(0))
             # ->있을땐 다음 거 들어와도 되는지 확인 
            if truck_weights:
                if sum(passing_queue)+truck_weights[0] <= weight:
                    passing_queue.append(truck_weights.pop(0))
                    passing_time_queue.append(0)
            
        # ->없다면
        else:
            # ->대기트럭 다리 건너게 하기
            passing_queue.append(truck_weights.pop(0))
            passing_time_queue.append(0)
        
       

        print(passing_time_queue)
        print(passing_queue)
       


    
    return answer

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))