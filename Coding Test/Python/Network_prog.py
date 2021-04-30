def solution(n, computers):
    
    visit = []

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    answer = 0

    for i in range(n):
        visit.append([0 for j in range(n)])
    
    for i in range(len(computers)):
        for j in range(len(computers[i])):

            if computers[i][j] ==1:

                #만약 체크하는 노드에 방문하지 않았을 때(네트워크가 다르다는 뜻)
                if visit[i][j] == 0 :
                    visit[i][j] = 1
                    print(visit)
                    answer += 1
            
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx >= 0 and ny >= 0 and nx < len(computers) and ny < len(computers):
                    #네트워크로 연결되어 있지만 방문하지 않은 컴터
                        if visit[nx][ny] == 0 and computers[nx][ny] == 1:
                            visit[nx][ny] = 1
            
    
    return answer

if __name__ == '__main__':
    
    print(solution(5, [[1, 1, 0, 0, 0], [1, 1, 0, 1, 0], [0, 0, 1, 0, 1], [1, 0, 0, 1, 1], [1, 1, 1, 0, 1]]))
