# 완전 탐색 (Brute Force)



- 가능한 모든 경우를 탐색 

- 반복문, 재귀함수를 이용해서 구현

- 리스트에 8이 어디에 있는지 알기 위한 완전 탐색 구현

  ```
  # 반복문
  def solution(trump):
  	for i in range(len(trump)):
  		if trump[i] == 8:
  			return i
  ```

  ```
  # 재귀함수
  def solution(trump, loc):
  	if trump[loc] == 8:
  		return loc
      else:
      	return solution(trump, loc+1)
  ```

  

