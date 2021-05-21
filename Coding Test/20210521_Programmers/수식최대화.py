import itertools

def calc(equation, operationPri, operandIdx):

    if operandIdx < len(operationPri):
        idx = equation.rfind(operationPri[operandIdx])
        if idx != -1:
            if operationPri[operandIdx] =='*':
                return calc(equation[:idx],operationPri,operandIdx) * calc(equation[idx+1:],operationPri,operandIdx)
            elif operationPri[operandIdx] =='-':
                return calc(equation[:idx],operationPri,operandIdx) - calc(equation[idx+1:],operationPri,operandIdx)
            elif operationPri[operandIdx] =='+':
                return calc(equation[:idx],operationPri,operandIdx) + calc(equation[idx+1:],operationPri,operandIdx)
        else:
            return calc(equation,operationPri,operandIdx+1)   

    
    return int(equation)

def solution(expression):
    answer = 0
    numbers = [] 
    operationTypes = set()
    
    #0 곱셈 항, 1 덧셈 항, 2 뺄셈 항 튜플로 저장
    operationDict ={}
    number = ''

    for i in range(len(expression)):
        if not expression[i].isdigit():
            operationTypes.add(expression[i])

    #계산 조합 순열
    operationOrders = list(map(list,itertools.permutations(operationTypes, len(operationTypes))))

    for i in range(len(operationOrders)):
        if answer < abs(calc(expression,operationOrders[-i],0)):
            answer =  abs(calc(expression,operationOrders[-i],0))


    return answer



print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
