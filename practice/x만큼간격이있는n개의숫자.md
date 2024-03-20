## 배열

```java
class Solution {
  public long[] solution(int x, int n) {
    long[] answer = new long[n];
    answer[0] = x;
    for(int i = 1; i < n; i++) {
      answer[i] = answer[i - 1] + x;
    }
    return answer;
  }
}
```

## 반복문 다른 것을 이용한 방법

```java
import java.util.stream.IntStream;

class Solution {
  public long[] solution(int x, int n) {
    long[] answer = new long[n];
    answer[0] = x;

    IntStream.range(1, n)
      .forEach(i -> {
        answer[i] = answer[i - 1] + x;
    });

    return answer;
  }
}
```

## LongStream을 이용한 방법

```java
import java.util.stream.LongStream;

class Solution {
  public long[] solution(int x, int n) {
    return LongStream.iterate(x, i->i+x).limit(n).toArray();
  }
}
```

### iterate

```java
static LongStream iterate(long seed, LongUnaryOperator f)
```

- seed: 스트림의 첫 번째 요소인 초기값
- f: 이전 요소를 입력으로 받아 다음 요소를 생성하는 함수
