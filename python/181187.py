import math

def solution(r1, r2):
    """
    Args:
        r1(Int): 원 1의 반지름 길이를 나타내는 정수
        r2(Int): 원 2의 반지름 길이를 나타내는 정수

    Returns:
        (Int): 두 원 사이의 공간에 x, y 좌표가 모두 정수인 점의 갯수
    """
    count = 0
    
    for x in range(1, r2 + 1):
        max_y = math.floor(math.sqrt(r2**2 - x**2))
        
        if x < r1:
            min_y = math.ceil(math.sqrt(r1**2 - x**2))
            
        else:
            min_y = 0
            
        count += max_y - min_y + 1
        
    return count * 4