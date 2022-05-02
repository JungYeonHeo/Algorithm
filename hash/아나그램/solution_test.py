"""
문제: Anagram이란 두 문자열이 알파벳의 나열 순서는 다르지만 그 구성이 일치하면 두 단어는 아나그램이라고 한다.
예를 들면 AbaAeCe와 BaeeACA는 알파벳을 나열 순서는 다르지만 그 구성을 살펴보면 A(2), a(1), b(1), C(1), e(2)로 알파벳과 그 개수가 모두 일치한다.
길이가 같은 두 개의 단어가 주어지면 두 단어가 아나그램인지 판별하는 프로그램을 작성

첫 줄에 첫 번째 단어가 입력되고, 두 번째 줄에 두번째 단어가 입력
두 단어가 아나그램이면 "YES"를 출력하고, 아니면 "NO"를 출력

<입력>
AbaAeCe
baeeACA

<출력>
YES
"""

# 딕셔너리 해쉬
# 방법 1  
import sys
# sys.stdin = open("input.txt", "r")
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x, 0) + 1 # x라는 알파벳이 없으면 값을 0으로 초기화, 있으면 해당 값에 +1 
for x in b:
    str2[x] = str2.get(x, 0) + 1 

for i in str1.keys():
    if i in str2.keys(): # str1에 존재하는 key값이 str2의 key값에도 존재하면 
        if str1[i] != str2[i]: # 같은 key에 해당하는 값이 다름
            print("NO")
            break
    else: # str1에 존재하는 key가 str2에 존재하지 않으면 
        print("NO")
        break
else: # 아나그램일 경우 = for문이 정상종료
    print("YES")




