def dfs(numbers, target, index, current_sum):
    if index == len(numbers):
        if current_sum == target:
            return 1
        return 0
    
    plus = dfs(numbers, target,
              index + 1, current_sum + numbers[index])
    
    minus = dfs(numbers, target,
               index + 1, current_sum - numbers[index])
    
    return plus + minus

def solution(numbers, target):
    """
    Args:
        numbers(List): 음이 아닌 양의 정수가 담긴 리스트
        target(Int): numbers 리스트 내 숫자의 순서를 바꾸지 않고, +/- 를 이용하여 만든 목표 숫자

    Returns:
        (Int): 목표 숫자를 만드는 경우의 수
    """
    return dfs(numbers, target, 0, 0)