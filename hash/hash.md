# 해시 (Hash)



- key, value 형태로 저장되어 검색과 저장이 빠르다 

- 해시함수: 임의의 길이를 갖는 메시지를 입력받아 고정된 길이의 해시값을 출력하는 함수

- 해시 구현 방법

  ```
  # 딕셔너리 삽입
  hash = dict()
  hash[1] = 'apple'
  hash['banana'] = 3
  hash[(4, 5)] = [1, 2, 3]
  hash[10] = dict({1: 'a', 2: 'b'}) 
  # 배열과 집합은 키값으로 사용할 수 없다.
  
  # 딕셔너리 수정
  hash[1] = 'melon'
  hash['banana'] = 10
  
  # 딕셔너리 값 추출
  hash.pop(1) # 'melon'
  hash.pop('banana') # 10
  hash.pop((4, 5)) # [1, 2, 3]
  hash.pop(10) # {1: 'a', 2: 'b'}
  
  # 딕셔너리 삭제 - 결과를 반환하지 않고 삭제
  del hash[1]
  del hash['banana']
  del hash[(4, 5)]
  del hash[10]
  ```

- 딕셔너리 활용

  ```
  # 딕셔너리 루프
  # hash = dict()
  # hash.keys() -> key 추출
  # hash.values() -> value 추출
  # hash.items() -> key와 value 추출
  
  hash = dict()
  for i in range(1, 6):
  	hash[i] = i ** 2
  	
  for k in hash.keys();
  	print(k) # 1 2 3 4 5 
  	
  for v in hash.values():
  	print(v) # 1 4 9 16 25
  	
  for k, v in hash.items():
  	print(k, v)
  	
  	
  # 딕셔너리 정렬
  # sorted 언제나 list 타입을 반환
  
  # 오름차순 정렬
  hash = dict({1:10, 3:12, 5:7, 7:6, 4:5})
  sorted(hash.keys(), key=lambda x:x) # [1, 3, 4, 5, 7]
  sorted(hash.values(), key=lambda x:x) # [5, 6, 7, 10, 12]
  sorted(hash.items(), key=lambda x:x) # [(1, 10), (3, 12), (4, 5), (5, 7), (7, 6)]
  
  # 내림차순 정렬
  hash = dict({1:10, 3:12, 5:7, 7:6, 4:5})
  sorted(hash.keys(), key=lambda x:-x) # [7, 5, 4, 3, 1]
  sorted(hash.values(), key=lambda x:-x) # [12, 10, 7, 6, 5]
  sorted(hash.items(), key=lambda x:-x) # ERROR 튜플에 -를 적용할 수 없기 때문에 
  sorted(hash.items(), key=lambda x:-x[1]) # [(3, 12), (1, 10), (5, 7), (7, 6), (4, 5)] 두번째 원소로 정렬
  sorted(hash.items(), key=lambda x:(x[0], x[1])) # key오름차순, value오름차순
  sorted(hash.items(), key=lambda x:(-x[0], x[1])) # key내림차순, value오름차순
  sorted(hash.items(), key=lambda x:(x[1], x[0])) # value오름차순, key오름차순
  ```

  
