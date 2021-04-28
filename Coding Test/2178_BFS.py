def main():
    N,M = map(int, input().split())
    data = [[0]*M for i in range(N)]
    visit = [[0]*M for i in range(N)]

    #Maze Map 초기화
    for i in range(N):
        map_in = input()
        for j,val in enumerate(map_in):
            data[i][j] = int(val)

    #상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    need_visit = list()

    need_visit.append((0,0))
    visit[0][0]=1
    while need_visit:
        x, y = need_visit.pop(0)
        if x == N-1 and y == M-1:
            print(visit[x][y])
            break
    
        #상하좌우 움직이기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            
                
            if nx >= 0 and nx<N and ny<M and ny >= 0:
                if data[nx][ny] == 1 and visit[nx][ny]==0:
                    visit[nx][ny] = visit[x][y]+1 
                    need_visit.append((nx,ny))

if __name__ == '__main__':
    main()