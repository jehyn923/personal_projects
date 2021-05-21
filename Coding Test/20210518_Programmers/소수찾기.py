import heapq
from itertools import permutations

def solution(numbers):
    primeNumbers = [2]
    primeDict = {2:1}
    availableNumbers = set()
    answer = 0
    
    for i in range(1, len(numbers)+1):
        numberPermutations = list(permutations(numbers,i))
        for j in range(len(numberPermutations)):
            availableNumbers.add(int(''.join(numberPermutations[j])))
    #print(availableNumbers)

    maxNum = max(availableNumbers)
    availableNumbers = list(availableNumbers)
    print(availableNumbers)
    
    for i in range(2, maxNum+1):
        isPrimeNum = True
        for j in range(len(primeNumbers)):
            if i % int(primeNumbers[j]) == 0:
                isPrimeNum = False
                break
        if isPrimeNum:
            primeNumbers.append(i)
            
            primeDict[i] = 1

    for i in range(len(availableNumbers)):
        if availableNumbers[i] in primeDict:
            answer+=1



    return answer

#solution("0")
#solution("17")
print(solution("011"))