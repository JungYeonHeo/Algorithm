# 연결리스트 (LinkedList)란?

- 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어 데이터를 저장하는 자료 구조

- List: 데이터를 인덱스 값에 따라 저장하므로 데이터의 추가와 삭제시 많은 시간 요구

- LinkedList: 데이터를 앞뒤 데이터에 따라 저장하므로 데이터의 추가화 삭제시 적은 시간 요구

- head: 가장 앞에 있는 변수를 담고 있는 노드

  ```
  class Node():
  	def __init__(self, data):
  		self.data = data
  		self.next = None
  		
  class LinkedList():
  	def __init__(self):
  		self.head = None
  		self.count = 0
  		
    def appendHead(self, node):
      if self.head == None:
          self.head = None
          self.count = 1
      else:
          self.count += 1 
          currentHead = self.head
          self.head = node 
          node.next = currentHead
      	
    def append(self, node):
      if self.head == None:
        self.head = node
        self.count = 1
      else:
        now = self.head
        while now.next != None:
          now = now.next
          now.next = node 
          self.count += 1
              
    def insertNodeAtIndex(self, node, index):
      if index < 0 or index > self.count:
        return -1
      elif self.count == index:
        self.append(node)
      elif index == 0:
        self.appendHead(node)
      else:
        now = self.head
        while index > 0:
          index -= 1
          now = now.next 
        self.count += 1
        next = now.next
        now.next = node
        node.next = next
          	
    def deleteData(self, data):
      if self.head.data == data:
        self.head = self.head.next
        self.count -= 1
      else:
        first = self.head 
        second = first.next
        while second != None:
          if second.data == data:
              first.next = second.next
              self.count -= 1
              break
          first = second 
          second = second.next
                  
    def getcount(self):
      return self.count
  ```

  