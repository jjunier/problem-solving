def solution(N, number):
    """
    Args:
        N(Int): 임의의 일의 자리 숫자
        number(Int): 숫자 N만을 사용하여 만들 숫자

    Returns:
        (Int): 숫자 N과 사칙연산을 사용하여 number를 만드는데에 사용한 횟수의 최솟값
    """
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    
                    if b != 0:
                        dp[i].add(a // b)
                        
        if number in dp[i]:
            return i
        
    return -1