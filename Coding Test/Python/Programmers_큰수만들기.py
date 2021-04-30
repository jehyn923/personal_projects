#시간초과
def solution(number, k):
    nums = []
    answer = []
    limit = k
    largest = 0
    largest_loc = 0

    #슬라이싱 후 max 
    #n-k번
    
    for i in range(len(number)):
        nums.append(int(number[i]))

    for i in range(len(number)-k):
        limit+=1
        largest=max(nums[largest_loc:limit])
        answer.append(str(max(nums[largest_loc:limit])))
        largest_loc = nums.index(largest,largest_loc,limit)+1
    
    answer = ''.join(answer)

    return answer

print(solution("1924",2)) #94
print(solution("1231234",3)) #3234
print(solution("4177252841",4)) #775841