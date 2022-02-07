# 다익스트라 (Dijkstra) : 최단 경로 알고리즘



- 다이나믹 프로그래밍을 활용한 대표적인 최단 경로 탐색 알고리즘

- 플로이드 와샬 알고리즘

  - 모든 노드를 방문하는 최단 경로

  ```
  values = [2 ** 31 - 1 for i in range(n)]
  visited = [False for i in range(n)]
  start = 0
  visited[start] = 0
  while False in visited:
  	for i in costs:
  		if visited[i[1]] == False and i[0] == start:
  			values[i[1]] = min(values[i[1]], i[2]])
          if visited[i[0]] == False and i[1] == start:
  			values[i[0]] = min(values[i[0]], i[2]])
      refer = 2 ** 31 - 1
      for i in range(n):
      	if visited[i] == False and values[i] != 0:
      		refer = min(refer, values[i])
      	answer = answer + refer
      	for i in range(n):
      		if visited[i] == False and values[i] == refer:
      			visited[i] = True
      			start = i 
      			break
  ```

- 다익스트라 알고리즘

  - 특정 노드에서 다른 노드까지의 최단 경로

  ```
  visited = [False for _ in range(n)]
  cost = [sys.maxsize for _ in range(n)]
  visited[0] = True
  cost[0] = 0
  length = len(visited)
  while False in visited:
  	checkLoc = -1
  	checkValue = sys.maxsize
  	for i in range(length):
  		if visited[i] == False and cost[i] < checkValue:
  			checkLoc = i
  			checkValue = cost[i]
          if checkLoc == -1:
          	break
          visited[checkLoc] = True
          for v1, v2, c in costs:
          	if v1 == checkLoc and visited[v2] == False:
          		cost[v2] == min(cost[v2], cost[v1] + c)
          	if v2 == checkLoc and visited[v1] == False:
          		cost[v1] == min(cost[v1], cost[v2] + c)
  ```

  
