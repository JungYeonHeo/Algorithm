# 프로그래머스 DFS&BFS 네트워크 
def solution(n, computers):
    answer = 0
    visited = [False for n in range(n)]
    
    while not all(visited):
        visited = dfs(visited.index(False), computers, visited)
        answer += 1
    
    return answer
            
def dfs(n, computers, visited):
    if not visited[n]:
        visited[n] = True
        for i in range(len(computers)):
            if i == n:
                continue
            if computers[n][i] == 1:
                visited = dfs(i, computers, visited)
                
    return visited