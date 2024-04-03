```java
class Solution {
  boolean solution(String s) {
    s = s.toLowerCase();
    return s.chars().filter(c -> c == 'p').count() == s.chars().filter(c -> c == 'y').count();
  }
}
```

- toLowerCase(): 문자열 소문자로 변환
- s.chars().filter(c -> c == 'p').count()
  - s.chars(): 문자열을 스트림으로 변환, 문자열을 구성하는 각 문자를 IntStream으로 반환
  - filter(c -> c == 'p'): 스트림에서 'p'와 일치하는 문자만 필터링
  - count(): 필터링된 요소의 수를 반환, long 타입으로 반환
