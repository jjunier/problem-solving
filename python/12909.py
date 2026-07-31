def solution(s):
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