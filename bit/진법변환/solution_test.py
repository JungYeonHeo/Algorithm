# 백준 2745번 진법 변환
N, B = input().split()
B = int(B)
result = 0

for i, j in enumerate(N):
    try:
        if int(j):
            result += int(j) * B ** (len(N)-i-1)
    except:
        result += (ord(j)-55) * B ** (len(N)-i-1)
        
print(result)