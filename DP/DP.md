# 동적계획법 (Dynamic Programming, DP)



- 하나의 큰 문제를 여러 개의 공통되는 작은 문제로 나누어서 작은 문제의 정답들을 결합하여 알고리즘을 푸는 과정

- 접근 방법

  - Bottom Up 방법: 작은 문제에서 큰 문제로 반복문 호출

    ```
    # 피보나치 
    def fib(n):
    	fibList = [1, 1]
    	for i in range(2, n+1):
    		fibList.append(fibList[i-2]+fibList[i-1])
        return fibList[-1]
    ```

  - Top Down 방법: 큰 문제에서 작은 문제로 재귀 호출

    ```
    # 피보나치
    def fib(n):
    	if n == 0 or n == 1:
    		return 1
        else:
        	return fib(n-1) + fib(n-2)
        	
    # 메모이제이션(Memoization): 배열 혹은 해시를 활용하는 것이 핵심
    memo = {0: 1, 1: 1}
    
    def fib(n):
    	if n in memo:
    		return memo[n]
    	else:
    		result = fib(n-1) + fib(n-2)
    		memo[n] = result
    		return result 
    ```


- 예시

  ```
  # data = [3, 4, 5, 6, 1, 2, 5] 이웃하지 않는 숫자들의 합의 최댓값은?
  
  def solution(data):
  	if len(data) == 1:
  		return data[0]
      result = [data[0], max(data[0], data[1])]
      for i in range(2, len(data)):
      	result.append(max(result[i-1], result[i-2] +data[i]))
      return result[-1]
  ```

  
