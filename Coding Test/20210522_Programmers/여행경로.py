def dfs(travelmap, destination, start):
    stack = []
    route = []
    
    stack.append(travelmap[start].pop())
    route.append(start)
    if len(travelmap[start] > 1):
        min()
    while stack:
        node = stack.pop()
        route.append(node)
        print(travelmap)
        try:
            stack.append(travelmap[node].pop())
        except:
            break
        


    return route

def solution(tickets):
    answer = []
    travelmap = {}
    destination = {}

    for i in range(len(tickets)):
        try:
            travelmap[tickets[i][0]].append(tickets[i][1])
        except:
            travelmap[tickets[i][0]]=[]
            travelmap[tickets[i][0]].append(tickets[i][1])

        try:
            destination[tickets[i][1]] += 1
        except:
            destination[tickets[i][1]] = 1

        
        travelmap[tickets[i][0]].sort(reverse=True)
    print(travelmap)
    print(destination)

    #print(dfs(travelmap))
    #print(travelmap)    
    return answer

solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
