# 깊이 우선 탐색 (DFS: Depth First Search)



### 특징

- 하나의 경우의 수에 대하여 모든 경우의 수를 조사하고 다음 경우의 수를 조사하면서 해를 찾는 과정
- 방문하는 순서대로 **stack**에 쌓고 방문이 끝나면 stack에서 pop하는 형태
- 하나의 정점에서 다른 정점으로 이동하되 더 이상 깊이 들어갈 수 없을 때까지 이동한 다음 마지막 정점에서 더 이상 방문할 지점이 없으면 이전 정점으로 되돌아 다음 정점을 방문



### 동작방식

 ![ex1](https://user-images.githubusercontent.com/94504613/147814547-61ff872c-de98-4a98-8779-c90dae57fab8.png)

DFS = 6, 5, 3, 1, 0, 2, 4, 7, 8, 9



### 대표코드

```
정점의 집합은 V, 간선의 집합은 E
void search(vertex v) {
   visited[v] = 1;
   for each vertex w adjacent to v
      if(!visited[w]) search(w);
}
```

인접리스트로 표현된 그래프의 간선수가 **E**이면, 방문 횟수도 간선수를 초과할 수 없으므로 탐색 연산시간은 O(E)에 가능



### 예시 문제 (미로찾기)

```
while len(stack) > 0: 
	now = stack.pop()
	if now == dest: 
		return True
	x = now[1] 
	y = now[0] 
	if x - 1 > -1: # 왼쪽으로 이동할 수 있다면
		if maps[y][x-1] == 0: 
			stack.append([y, x-1])
			maps[y][x-1] = 2
	if x + 1  < hori: # 오른쪽으로 이동할 수 있다면, hori = x 좌표 끝
		if maps[y][x+1] == 0: 
			stack.append([y, x+1])
			maps[y][x+1] = 2 
	if y - 1 > -1: # 위로 이동할 수 있으면
		if maps[y-1][x] == 0: 
			stack.append([y-1, x])
			maps[y-1][x] = 2
	if y + 1 < verti: # 아래로 이동할 수 있다면, verti = y 좌표 끝
		if maps[y+1][x] == 0: 
			stack.append([y+1, x])
			maps[y+1][x] = 2
return False
```

