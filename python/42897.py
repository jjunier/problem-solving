def solution(money):
    """
    Args:
        money(List): 각 집에 있는 돈이 담긴 리스트

    Returns:
        (Int): 도둑이 놓칠 수 있는 돈의 최댓값
    """
    n = len(money)
    
    first_case = [0] * n
    first_case[0] = money[0]
    first_case[1] = max(money[0], money[1])
    
    for i in range(2, n - 1):
        first_case[i] = max(
            first_case[i - 1], 
            first_case[i - 2] + money[i]
        )
    
    second_case = [0] * n
    second_case[0] = 0
    second_case[1] = money[1]
    
    for i in range(2, n):
        second_case[i] = max(
            second_case[i - 1], 
            second_case[i - 2] + money[i]
        )
        
    return max(first_case[n - 2], second_case[n - 1])
    