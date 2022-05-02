# 방법 3: 리스트, 아스키값 사용 
import sys
# sys.stdin = open("input.txt", "r")
a = input()
b = input()
str1 = [0] * 52
str2 = [0] * 52
for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1
    else: 
        str1[ord(x) - 71] += 1
for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else: 
        str2[ord(x) - 71] += 1       
"""
if str1 == str2: # python식 비교
    print("YES")
else:
    print("NO")
"""

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")