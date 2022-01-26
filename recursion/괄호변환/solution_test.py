# 프로그래머스 재귀함수 괄호변환

def correct(u):
    r = {"(":")", ")": "("}
    return ''.join([r[i] for i in u])

def divide(p):
    if p == '': return p
    v = p; u = '';
    left = right = 0
    iscorrect = True
    if v == '':
        return v
    for i in range(len(v)):
        if v[i] == '(': left += 1
        if v[i] == ')': right += 1
        u += v[i]
        if right > left:
            iscorrect = False
        if left == right:
            if iscorrect == False:
                return '(' + divide(v[i+1:]) + ')' + correct(u[1:-1])
            else:
                return u + divide(v[i+1:])
        
def solution(p):
    answer = ''
    answer += divide(p)
    return answer