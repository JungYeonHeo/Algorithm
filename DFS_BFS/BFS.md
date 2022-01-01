# 너비 우선 탐색 (BFS: Breadth First Search)



### 특징

- 하나의 경우의 수에 대한 다음 단계의 모든 경우의 수를 조사하면서 해를 찾는 과정
- **Queue**의 성질을 활용하여 먼저 넣은 정점을 항상 먼저 방문
- 시작 정점을 방문한 후 시작 정접과 인접한 정점들을 우선적으로 방문하는 방식으로 임의의 정점을 방문하면 해당 정점의 인접한 정점을 우선적으로 방문하는 방식의 탐색 알고리즘 (연결되어 있지 않아도 근처에 있는 것을 먼저 방문)



### 동작방식

![ex3](https://user-images.githubusercontent.com/94504613/147846891-4ae34036-5df6-4357-bc78-09f75dc2a588.png)

- 정점 A에서 탐색: A->**B->H** 또는 A->**H->B**

- 정점 B에서 탐색: A->B->H->**C->F** 

​                   또는 A->B->H->**F->C**

- 정점 C에서 탐색: A->B->H->C->F->D

- 정점 D에서 탐색: A->B->H->F->C->D->G (E) 

​                 또는 A->B->H->F->C->G->D (E)



### 문제 예시 - 최단경로 구하기

```queu
while len(queue) > 0:
	count = len(queue)
	for time in range(count):
		now = queue.pop(0)
		if now == dest:
			return answer
        for i in data:
        	if i[0] == now and visited[i[1]-1] == False:
        		queue.append(i[1])
        		visited[i[1]-1] = True
        	elif i[1] == now and visited[i[0]-1] == False:
        	queue.append(i[0])
        	visited[i[0]-1] = True
    answer += 1
return answer
```

