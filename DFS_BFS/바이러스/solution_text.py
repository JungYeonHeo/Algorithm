# 백준 2606번 바이러스

num = int(input())
link = int(input())
num_list = []

i = 0
while i < link:
    num_list.append(input().split())
    i = i + 1 

virus = ['1']
p = 0

while True:
    for i in range(0,2):
        for j in range(0, link):
            if num_list[j][i] == virus[p]: 
                if i == 0 and num_list[j][1] not in virus:
                    virus.append(num_list[j][1])
                elif i == 1 and num_list[j][0] not in virus:
                    virus.append(num_list[j][0])
        
    p = p + 1

    try:
        virus[p] 
    except Exception as e:
        break

print(len(set(virus)) - 1)
