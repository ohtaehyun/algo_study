def solution(phone_book):
    phone_book.sort()
    for i in range(1,len(phone_book)):
        if phone_book[i].startswith(phone_book[i-1]):
            return False
    return True

solution(	["119", "97674223", "1195524421"] )