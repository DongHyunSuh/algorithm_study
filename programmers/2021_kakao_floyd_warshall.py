def solution(n, s, a, b, fares):
    graph = [[int(1e9)] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        # distance to self
        graph[i][i] = 0
    for src, dst, val in fares:
        graph[src][dst] = val
        graph[dst][src] = val
    for t in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dst = min(graph[i][j], graph[i][t] + graph[t][j])
                graph[i][j] = graph[j][i] = dst
    answer = int(1e9)
    for t in range(1, n+1):
        dst = graph[s][t] + graph[t][a] + graph[t][b]
        answer = min(answer, dst)
    return answer