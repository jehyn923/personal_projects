def solution(places):
    answer = []

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    

    for wholecase in range(len(places)):
        #전체 케이스 확인
        manhattan_good = True
        attendant = []
        map = {}
        map.clear()
        for i in range(len(places[wholecase])):
            for j in range(len(places[wholecase][i])):
                if places[wholecase][j][i]=='P':
                    map[(j,i)] =[]
                    attendant.append((j,i))
                for directions in range(4):
                    nx = j + dx[directions]
                    ny = i + dy[directions]
                
                    if nx >= 0 and ny >= 0 and nx < len(places[wholecase]) and ny < len(places[wholecase]):
                        #맵 밖으로 나갈 경우
                        if places[wholecase][nx][ny]=='P' or places[wholecase][nx][ny]=='O':
                            try:
                                map[(j,i)].append((nx,ny))
                            except:
                                map[(j,i)] = [] 
                                map[(j,i)].append((nx,ny))
    
        for i in range(len(attendant)):
            visited = []
            queue = []
            distance = 0 
            queue.append(attendant[i])
            move_distance_x = 0
            move_distance_y = 0
            print("start")
            print(attendant)
            print(attendant[i])
           # print(map)
            while queue:
                node = queue.pop(0)
           
                if node in attendant:
                    if node != attendant[i]:
                        if abs(node[0]-attendant[i][0])+abs(node[1]-attendant[i][1])<=2:
                            if node[0]-attendant[i][0] == 0:
                                if move_distance_x <= 2:
                                    mahattan_good = False
                            elif node[1]-attendant[i][1] == 0:
                                if move_distance_y<=2:
                                    manhattan_good = False

                            #print(node)
                            #print(move_distance_x,move_distance_y)

                if node not in visited:
                    if node[0]-attendant[i][0] == 0:
                        move_distance_y +=1
                    elif node[1]-attendant[i][1] == 0:
                        move_distance_x +=1    
                    visited.append(node)
                    queue.extend(map[(node)])
                
            #print(visited)
        if manhattan_good:
            
            
            print("YES")
            answer.append(1)
        else:
            answer.append(0)
        
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

