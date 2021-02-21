import heapq

def solution(n, s, a, b, fares):
    link = [[] for _ in range(n+1)]
    for src, dst, val in fares:
        # save distance info
        link[src].append((val, dst))
        link[dst].append((val, src))
    def dijkstra(start):
        dist = [int(1e9)] * (n+1)
        dist[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))
        while heap:
            val, dst = heapq.heappop(heap)
            if dist[dst] < val:
                continue
            for item in link[dst]:
                v, d = item[0], item[1]
                nval = val + v
                if dist[d] > nval:
                    dist[d] = nval
                    heapq.heappush(heap, (nval, d))
        return dist
    graph = [[]] + [dijkstra(i) for i in range(1, n+1)]
    answer = int(1e9)
    for i in range(1, n+1):
        answer = min(graph[i][a] + graph[i][b] + graph[i][s],
                    answer)
    return answer