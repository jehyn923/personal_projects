def solution(n, k, cmd):
    answer = ''
    cnt = 0
    result =['O' for i in range(n)]
    existing_table = [i for i in range(n)]
    pos = k 
    
    queue = []
    deleted = [] #스택으로 되돌리기 구현
    
    for i in range(len(cmd)):
        queue.append(cmd[i])          
    
    while queue:
        node = queue.pop(0)
        if node[0] == 'D':
            pos = pos+int(node[2])
        
        elif node[0] =='U':
            pos = pos-int(node[2])

        elif node[0] == 'C':
            result[existing_table[pos]] = 'X'

            deleted.append(existing_table[pos])

            del existing_table[pos]
            if pos == len(existing_table):
                pos -= 1
                             
        elif node[0] == 'Z':
            rewind=deleted.pop()
            result[rewind] = 'O'
            print(result)
            if rewind<existing_table[pos]:
                pos+=1
            existing_table.append(rewind)

            existing_table.sort()
        
        print(pos)
        print(existing_table)
    for i in range(len(result)):
        answer += str(result[i])
    
    return answer

#solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])