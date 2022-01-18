# 재귀함수 (Recursion)



- 메소드 혹은 함수의 내부에서 자기자신의 메소드 혹은 함수를 다시 호출하는 함수

- 반복문을 활용한 완전탐색

  ```
  data = [3, 5, 8]의 부분 집홥 구하기 
  
  result = set()
  for i in range(2):
  	for j in range(2):
  		for k in range(2):
  			result.add(data[0] * i + data[1] * j + data[2] * k)
  print(result)
  # 성분의 개수 = 반복문의 개수
  ```

- 재귀함수를 활용한 완전탐색

  ```
  # 재귀함수 사용 이유: 코드의 간결화 및 변수 사용 최소화
  
  data = [3, 5, 8]
  def recur(index, value) 
  	if (index == len(data)):
  		result.add(value)
      else:
      	recur(index + 1, value + data[index])
      	recur(index + value)
      	
  result = set()
  revur(0, 0)
  print(result)
  # 배열의 길이가 길어져도 함수의 수정 없이 사용할 수 있음
  ```

- 재귀함수 활용: 팩토리얼

  ```
  def factorial(n):
  	if n == 1:
  		return 1
     	else:
     		return n * factorial(n-1)
  
  factorial(5) 
  ```

- 재귀함수 활용: 피보나치

  ```
  def fibonacci(n):
  	if n == 0 or n == 1:
  		return 1
      else:
      	return fibonacci(n-1) + fibonacci(n-2)
  ```

  
