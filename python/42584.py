def solution(prices):
    """
    Args:
        prices(List): 초 단위로 기록된 주식 가격이 담긴 리스트

    Returns:
        prices_fall(List): 가격이 떨어지지 않는 기간이 몇 초인지 담긴 리스트
    """
    n = len(prices)
    prices_fall = [0] * n
    stack = []
    
    for current_index, current_price in enumerate(prices):
        while(stack and prices[stack[-1]] > current_price):
            previous_index = stack.pop()
            prices_fall[previous_index] = current_index - previous_index
            
        stack.append(current_index)
        
    last_index = n - 1
    
    while stack:
        previous_index = stack.pop()
        prices_fall[previous_index] = last_index - previous_index
        
    return prices_fall