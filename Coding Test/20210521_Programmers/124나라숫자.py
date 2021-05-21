#5억번의 경우, n번을 돌아도 효율성 터짐
#그렇기 때문에 n개의 124진법을 모두 구하지 않고 몫의 몫과 나머지를 구하는 재귀를 통해 구하는 것이 중요
#재귀 함수로도 구현 가능함. 3진법 변환과 과정은 같지만, 10 => 4, 20 => 14와 같은 작업이 까다로웠음
def solution(n):
    answer = ''
    decimalExpression = {1:'1', 2:'2', 0:'4'}
   
    number = []


    while n > 0:
        number.append(decimalExpression[n%3])
        if n % 3 == 0:
            n = n//3 - 1
        else:
            n = n//3
    for i in range(len(number)):
        answer += number.pop()
    print(answer)
       
    
    #newDecimal을 돌아 각 수의 124진법을 적용한 숫자를 저장하는 메모이제이션 기법 사용
    #for i in range(1, len(newDecimal)):
        
    #    if i < 4:
    #        newDecimal[i] += decimalExpression[i]
    #        continue

    #    if i % 3 == 0:
    #        newDecimal[i] += str(newDecimal[i//3-1]) + str(newDecimal[3])
    #    else:
    #        newDecimal[i] += str(newDecimal[i//3]) + str(newDecimal[i%3])

    #answer = newDecimal[n]
    #print(answer)
    
    return answer

solution(1)
solution(2)
solution(3)
solution(4)
solution(5)
solution(6)
solution(7)
solution(8)
solution(9)
solution(10)

solution(22)
solution(19)
solution(28)
solution(27)