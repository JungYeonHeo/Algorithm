from itertools import permutations
from math import sqrt, floor

def is_prime(num): # 소수인지 판단하는 함수
    if num < 2:
        return False

    for n in range(2, floor(sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True


def solution(numbers):
    answer = []
    numbers = list(numbers) # 문자열을 리스트로 변형
    for n in range(1, len(numbers) + 1):
        nums = [int("".join(num)) for num in permutations(numbers, n)] # permutations를 패키지를 사용하여 리스트로 조합이 가능한 길이가 n인 문자열을 생성 

        for num in nums:
            if is_prime(num) and (num not in answer): # 소수이고 중복되지 않으면 배열에 추가
                answer.append(num)

    return len(answer)