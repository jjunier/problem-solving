def solution(numbers):
    """
    Args:
        numbers: 이어 붙여 만들 수 있는 0 또는 양의 정수가 담긴 리스트
    
    Returns:
        (Int): 이어 붙여 만든 가장 큰 정수
    """
    numbers = list(map(str, numbers))
    
    numbers.sort(
        key=lambda x : x * 4,
        reverse=True
    )
    
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return '0'
    
    return answer