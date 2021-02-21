import sys
import heapq

N = int(sys.stdin.readline()) # node
M = int(sys.stdin.readline()) # line
graph = [[] for _ in range(N+1)]
INF  = int(1e9)
dist = [[INF, ''] for _ in range(N+1)]

for _ in range(M):
    src, dst, val = map(int, sys.stdin.readline().split())
    graph[src].append([val, dst])

start, end = map(int, sys.stdin.readline().split())
dist[start][0] = 0
dist[start][1] = str(start)

heap = []
heapq.heappush(heap, (0, start))

while heap:
    val, dst = heapq.heappop(heap)
    if dist[dst][0] < val:
        continue
    for v, d in graph[dst]:
        nval = val + v
        if dist[d][0] > nval:
            dist[d][0] = nval
            dist[d][1] = dist[dst][1] + '-' + str(d)
            heapq.heappush(heap, (nval, d))

print(dist[end][0])
print(len(dist[end][1].split('-')))
print(*dist[end][1].split('-'))