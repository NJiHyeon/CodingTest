def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1) :
        if phone_book[i+1].startswith(phone_book[i]) :
            return False
    return True


# 해시 개념을 이용해 풀이
'''
def solution(phone_book) :
    answer = True
    hash_map = {}
    for phone_number in phone_book :
        hash_map[phone_number] = 1
    for phone_number in phone_book :
        temp = ""
        for number in phone_number :
            temp += number
            if temp in hash_map and temp!= phone_number :
                answer = False
    return answer
'''