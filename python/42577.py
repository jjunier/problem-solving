def solution(phone_book):
    """
    Args:
        phone_book: 전화번호부 리스트 (List)
    
    Returns:
        True or False: 앞의 번호가 다른 번호의 접두어 여부 (boolean)
    """
    phone_set = set(phone_book)
    
    for number in phone_book:
        for i in range(1, len(number)):
            prefix = number[:i]
            
            if prefix in phone_set:
                return False
            
    return True