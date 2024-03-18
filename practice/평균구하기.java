import java.util.*;
import java.lang.*;

class Solution {
  public double solution(int[] arr) {
    return Arrays.stream(arr).average().getAsDouble();
    /**
     * getAsDouble()
     * double 값을 포함하거나 포함하지 않을 수 있는 래퍼 클래스
     * double은 null 값을 가질 수 없기 때문에, 값이 없는 상황을 나타내기 위해 OptionalDouble 클래스가 사용
     * OptionalDouble 객체를 사용할 때는 .isPresent() 메서드로 값이 존재하는지 확인한 후에, 값이 존재할 경우에만 .getAsDouble() 메서드를 통해 값을 가져올 수 있다.
     */
  }
}