# 백준 1260 DFS와 BFS

from collections import  deque

n, m, v = map(int, input().split())

list1 = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    list1[a].append(b)
    list1[b].append(a)
    list1[a].sort()
    list1[b].sort()


visited = [False] * (n + 1)

def dfs(list1, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in list1[v]:
        if not visited[i]:
            dfs(list1, i, visited)

def bfs(list1, v, visited):
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True
    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        for i in list1[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(list1, v, visited)
print()
bfs(list1, v, visited)
