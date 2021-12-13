# 스택 (Stack)



- **LIFO(Last In First Out)** 후입선출 - 입구와 출구가 하나밖에 없는 구조

- 시간복잡도: **O(1)**

- **top**(Stack Pointer)를 사용하여 가장 나중에 입력된 데이터의 위치를 가리킨다.

- **bottom**은 막혀있는 다른 한 쪽 끝을 가리킨다.

- 배열로 스택 구현 - 삽입 (**push**)

  ```
  void push(element item) {
   if(top >= MAX_STACK_SIZE - 1)
      stackfull();
   stack[++top] = item; 
   /* 위치 증가시킨 후 데이터입력 */
  }
  ```

- 배열로 스택 구현 - 삭제 (**pop**)

  ```
  element pop() {
   if (top == -1) 
      return stakempty();
   return stack[top--]; 
   /* 데이터 출력 후 위치 감소 */ 
  }
  ```

- 스택 응용
  - 복귀주소관리(서버루틴호출, 인터럽트)
  - 순환(Recursion)
  - 산술연산
  - 연산표기식
  - 이진트리 순회(전위, 중위, 후위)
  - 퀵 정렬
  - 깊이우선 탐색
  - 텍스트 에디터에서의 작업 취소(undo) 과정 





# 큐 (Queue)



### 1. 큐 

- **FIFO(First In First Out )** 선입선출 - 먼저 입력된 데이터부터 앞쪽에서 출력하고 입력은 다른쪽으로 함
- 시간복잡도: **O(1)**

- 배열로 큐 구현 - 삽입(**push**)

  ```
  void addq(element item) { 
  /* queue에 item 삽입 */
   if(rear == MAX_QUEUE_SIZE - 1)
      queueFull();
   queue[++rear] = item;
  }
  ```

- 배열로 큐 구현 - 삭제(**pop**)

  ```
  element deleteq() {
  /* queue의 앞에 있는 원소를 삭제 */
   if (front == rear) 
      return queueEmpty();
   return queue[++front];
  }
  ```

- **enqueue()**: 데이터를 입력하는 함수
- **dequeue()**: 데이터를 출력하는 함수 
- **peek()** : 큐가 비어있지 않으면 맨 앞의 요소를 삭제하지 않고 반환한다.
- **rear**: tail(뒤), 삽입이 발생하는 부분, 제일 마지막에 있는 자료를 가리킨다.
- **front**: head(앞), 삭제가 발생하는 부분, 제일 앞에 있는 자료보다 1 작은 위치를 가리키거나 삭제한 위치를 가리킨다.
- front와 rear의 초기치: **–1** ([0]부터 데이터 삽입됨)
- 큐의 응용
  - 작업 스케줄링
  - 버스 줄서기
  - 그래프의 너비 우선 탐색
  - 트리의 level 순회
  - 스풀링
  - 비동기적 데이터 전송 (파일 입출력, 파이프, 소켓)



### 2. 원형 큐 

- 원형 큐의 경우 **하나의 공간을 비워둔다**. 
  - 비어있는 공간이 하나 없다면 꽉 찬 큐와 텅 빈 큐를 구별할 수 없게 된다.
  - 10(MAX_QUEUE_SIZE)개의 큐일 경우 9의 자료를 저장할 수 있다.
- 원형 큐가 꽉 찬 상태(Full): **front = (*rear + 1) % MAX_QUEUE_SIZE;**  
- 원형 큐가 빈 상태(Empty): rear과 front가 같은 공간에 있다. **front == rear** 
- 초기 값 보통 front, rear 모두 **0** 이다. 
- **rear**는 처음 값을 삽입하면 [1]번째부터 값이 들어간다.
  - 포화상태(원형 큐 크기보다 1 작을 때)이면 데이터 삽입이 이루어지지 않는다. 
- **front**는 방금 삭제한 곳을 가리킨다. 

- 배열로 원형 큐 구현 - 삽입

  ```
  void addq(element item) { 
  /* queue에 item 삽입 */
   if((rear+1) mod(%) MAX_QUEUE_SIZE == front) /* 포화 */
      queueFull(); 
   rear = (rear + 1) mod MAX_QUEUE_SIZE;
  ```

- 배열로 원형 큐 구현 - 삭제

  ```
  element deleteq() {
  /* queue의 앞에 있는 원소를 삭제 */
   if (front == rear) /* 공백 */
      return queuEempty(); 
   return queue[front];
  ```



### 3. 데크 (Deque: Double-ended queue)

- 양쪽 끝에서 추가와 삭제가 가능한 선형 리스트

- 스택과 큐를 하나의 선형리스트 구조로 혼합시킨 형태

- 두 개의 스택의 bottom 부분을 서로 연결시켜 큐 모양이 되게 한다.

- **L-bottom**: 왼쪽 끝에서 삽입과 삭제가 일어날 위치를 가리키고, 제일 왼쪽 자료를 가리킨다.

- **R-bootom**: 오른쪽 끝에서 삽입과 삭제가 일어날 위치를 가리키고 제일 오른쪽 자료를 가리킨다.

- 스크롤: 입력이 한 쪽 끝으로만 가능하도록 설정한 데크 (입력 제한 데크)

- 셀프: 출력이 한 쪽 끝으로만 가능하도록 설정한 데크 (출력 제한 데크)

- 시간복잡도 

  insertFirst: 데크의 첫 번째 원소로 삽입 -> O(1) 

  insertLast: 데크의 마지막 원소로 삽입 -> O(1)

  deleteFirst: 데크의 첫 번째 원소를 삭제 -> O(1)

  **deleteLast:** **데크의 마지막 원소를 삭제** **-> O(n)** 

  (마지막 노드 삭제는 마지막 노드의 선행 노드를 찾아야 하기 때문에 리스트의 처음부터 끝까지 추적해야 해서 O(n) 이다.)

