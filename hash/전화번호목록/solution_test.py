def solution(phone_book):
    answer = True
    phone_book.sort(key=len)

    if len(phone_book) > 1:
        for i in range(len(phone_book)-1):
            for j in range(i+1, len(phone_book)):
                if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                    return False

    return answer