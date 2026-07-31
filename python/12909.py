def solution(s):
    """
    Args:
        s(List): '('와 ')'로만 이루어진 문자열 리스트
    
    Returns:
        (Boolean): s 리스트에 담긴 괄호 문자열들의 열리고 닫힘이 올바른 형태인지에 대한 참/거짓
    """
    if s[0] == ')' or s[-1] == '(' or len(s) % 2 == 1:
        return False
    
    bracket_count = 0
    
    for bracket in s:
        if bracket == '(':
            bracket_count += 1
        
        else:
            bracket_count -= 1
            
        if bracket_count < 0:
            return False
        
    if bracket_count != 0:
        return False

    return True