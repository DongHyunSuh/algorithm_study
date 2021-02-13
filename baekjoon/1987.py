import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def DFS(x, y, ans):
    global answer
    answer = max(ans, answer)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if ((0 <= nx < R) and (0 <= ny < C)) and not visited[ord(board[nx][ny])-65]:
            visited[ord(board[nx][ny])-65] = True
            DFS(nx, ny, ans+1)
            visited[ord(board[nx][ny])-65] = False



R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

#append and pop -> time out
visited = [False] * 26
visited[ord(board[0][0])-65] = True

answer = 1
DFS(0, 0, answer)
print(answer)