import heapq
import sys

N = int(sys.stdin.readline())
x = []
queue=[]

for i in range(N):
    x=int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(queue, -1*x)
    else:
        if not queue:
            print(0)
        else:
            print(-1 * heapq.heappop(queue))

 