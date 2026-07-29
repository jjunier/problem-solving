def solution(clothes):
    '''
    Args:
        clothes: 의상의 이름들과 의상의 종류 (2차원 리스트)
    
    Returns:
        (int): 입을 수 있는 의상의 모든 경우의 수
    '''
    
    clothes_dict = {}
    answer = 1
    
    for name, category in clothes:
        clothes_dict[category] = clothes_dict.get(category, 0) + 1
        
    for count in clothes_dict.values():
        answer *= (count + 1)
        
    return answer - 1

