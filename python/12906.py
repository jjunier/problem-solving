def solution(arr):
    """
    Args:
        arr(List): 0부터 9까지 숫자가 담긴 리스트
    
    Returns:
        (List): 연속적으로 반복되는 숫자들을 제거한 리스트
    """
    answer = []
    
    for number in arr:
        if not answer or answer[-1] != number:
            answer.append(number)
    
    return answer