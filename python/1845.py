def solution(nums):
    """
    Args:
        nums(List): 종류에 따라 번호로 분류된 폰켓몬
        
    Returns:
        integer: n // 2개에서 가질 수 있는 폰켓몬 최대 종류 가짓수
    """
    
    return min(len(nums) // 2, len(set(nums)))