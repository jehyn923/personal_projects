def solution(n, arr1, arr2):
    answer = []
    new_map = []

    for i in range(n):
        #지도 1, 지도 2 합친 후 새로운 Map 만들어냄
        new_map.append(arr1[i]|arr2[i])
    
    for i in range(n):
        
        #위 or 연산 숫자 binary화 한 다음 string화
        binary_map=str(bin(new_map[i]))
        #0b <- 해당 수식어 없애야 하기 때문에 슬라이싱
        binary_map=binary_map[2:]

        binary_map=binary_map.zfill(n)
        
        #Replace O(n^2)이라고 함. 바꿀 수 있는 방법을 찾아보는 것이 좋을듯
        binary_map = binary_map.replace("1","#")
        binary_map = binary_map.replace("0"," ")
        
        answer.append(binary_map)
        
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))

