def solution(name):
    """
    Args:
        name(String): 조이스틱으로 만들고자 하는 이름

    Returns:
        (Int): 이름을 만들기 위한 최소한의 조이스틱 조작 횟수
    """
    answer = 0
    
    for char in name:
        up = ord(char) - ord('A')
        down = ord('Z') - ord(char) + 1
    
        answer += min(up, down)
        
    move = len(name) - 1
    
    for i in range(len(name)):
        next_index = i + 1
        
        while(next_index < len(name)
             and name[next_index] == 'A'):
            next_index += 1
            
        move = min(move, i * 2 + len(name) - next_index)
        
        move = min(move, (len(name) - next_index) * 2 + i)
        
    return answer + move