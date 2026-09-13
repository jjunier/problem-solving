def solution(arr):
    """
    Args:
        arr(List): 두 연산자가 덧셈과 뺄셈, 숫자가 들어있는 리스트

    Returns:
        (Int): 서로 다른 연산 순서의 계산 결과 중 최댓값
    """
    numbers = []
    operators = []
    
    for i in range(len(arr)):
        if i % 2 == 0:
            numbers.append(int(arr[i]))
        
        else:
            operators.append(arr[i])
            
    n = len(numbers)
    
    max_result = [[float('-inf')] * n for _ in range(n)]
    min_result = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        max_result[i][i] = numbers[i]
        min_result[i][i] = numbers[i]
        
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            
            for k in range(start, end):
                operator = operators[k]
                
                if operator == '+':
                    max_value = (max_result[start][k] + max_result[k + 1][end])
                    min_value = (min_result[start][k] + min_result[k + 1][end])
                    
                else:
                    max_value = (max_result[start][k] - min_result[k + 1][end])
                    min_value = (min_result[start][k] - min_result[k + 1][end])
                    
                max_result[start][end] = max(max_result[start][end], max_value)
                min_result[start][end] = min(min_result[start][end], min_value)
                
    return max_result[0][n - 1]