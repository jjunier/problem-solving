def solution(number, k):
    """
    Args:
        numbers(String): 문자열 형식의 숫자
        k(Int): numbers에서 제거할 숫자 갯수

    Returns:
        (String): numbers에서 k개 만큼 제거한 숫자 중에서 가장 큰 숫자를 문자열 형태로 변환
    """
    stack = []
    
    for digit in number:
        while(stack and k > 0 and stack[-1] < digit):
            stack.pop()
            k -= 1
            
        stack.append(digit)
        
    if k > 0:
        stack = stack[:-k]
        
    return ''.join(stack)