from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q.append([i, j])
    w = [[0]*m for _ in range(n)]
    w[i][j] = 1
    t = 0
    while q:
        i, j = q.popleft()
        for k in range(4):
            _i = i + dx[k]
            _j = j + dy[k]
            if 0 <= _i < n and 0 <= _j < m:
                if l[_i][_j] == 'L' and w[_i][_j] == 0:
                    w[_i][_j] = w[i][j] + 1
                    t = max(t, w[_i][_j])
                    q.append([_i, _j])
    return t-1

n, m = map(int, input().split())
l = [list(input()) for _ in range(n)]
q = deque()
cnt = 0

for i in range(n):
    for j in range(m):
        if l[i][j] == 'L':
            cnt = max(cnt, bfs(i, j))
print(cnt)