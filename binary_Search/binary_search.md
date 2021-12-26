# 이분 탐색 (Binary Search)



- 개수가 정해진 자연수를 크기순으로 저장하고 탐색하기에 가장 적절한 방법

- 정렬된 경우에만 사용 가능 

- 평균 시간 복잡도 O(  ![img](file:///C:\Users\hjy\AppData\Local\Temp\DRW00002b903a86.gif)  )

- 전위순회 형식

- 자료의 수가 1024개인 경우 2진 탐색을 하였을 때 최대 비교 횟수:  ![img](file:///C:\Users\hjy\AppData\Local\Temp\DRW00002b903a7a.gif)   

  ```
  int binSearch(int *a, int key, int low, int high) {
     int middle;
     while(low <= high) {
        middle = (low + high) / 2;
        if (key == a[middle])
           return middle;
        else if (key > a[middle])
           low = middle + 1;
        else
           high = middle – 1; 
     }
     return -1;
  }
  ```

  

  

