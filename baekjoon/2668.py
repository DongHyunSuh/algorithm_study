def dfs(v, i):
    vis[v] = True
    num = nums[v]
    if not vis[num]:
        dfs(num, i)
    elif vis[num] and num == i: # cycle
        res.append(num)

N = int(input())
nums = [0] # tmp val
for _ in range(N):
    nums.append(int(input()))
res  = []

for i in range(1, N+1):
    vis  = [False] * (N+1)
    dfs(i, i)
    
print(len(res))
for n in res:
    print(n)