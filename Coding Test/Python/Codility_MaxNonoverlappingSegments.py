def solution(A,B):
    segment = 0
    num_non_seg = 0
    N = len(A)
    non_segment = [] 

    for i in range(N):
        
        if non_segment:
            if A[i] > B[non_segment[-1]]:
                non_segment.append(i)
        else:
            non_segment.append(i)
        
        if num_non_seg < len(non_segment):
            num_non_seg = len(non_segment)
 
    answer = num_non_seg
    return answer


A = [1,3,7,9,9]
B = [5,6,8,9,10]

print(solution([1,3,7,9,9],[5,6,8,9,10]))