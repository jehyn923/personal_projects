def bfs(network, start_point):
    visited = list()
    need_visit = list()
    
    #출발 지점
    need_visit.extend(start_point)
    
    while need_visit:
        comp = need_visit.pop(0)
        if comp not in visited:
            visited.append(comp)
            need_visit.extend(network[comp])
    
    #진원지 제거
    return len(visited)-1

if __name__ == "__main__":

    comp_num = int(input())
    network_num = int(input())

    #네트워크 초기화
    network = dict()
    for i in range(1,comp_num+1):
        network[i] = list()
    for i in range(network_num):
        a, b = map(int,input().split())

        network[a].append(b)
        network[b].append(a)

    print(bfs(network,network[1]))