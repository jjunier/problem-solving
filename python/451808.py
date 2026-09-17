from itertools import permutations

def get_score(guess, candidate):
    strike, ball = 0, 0
    
    for i in range(4):
        if guess[i] == candidate[i]:
            strike += 1
        elif guess[i] in candidate:
            ball += 1
            
    return f"{strike}S {ball}B"

def solution(n, submit):
    """
    Args:
        n(Int): 4자리 숫자(1000~9999)를 제출할 수 있는 최대 기회

    Returns:
        (Int): 서로 다른 숫자 4개로 이루어진 숫자 야구 비밀번호
    """
    candidates = [
        ''.join(numbers)
        for numbers in permutations('123456789', 4)
    ]
    
    submit_count = 0
    
    while candidates and submit_count < n:
        guess = candidates[0]
        
        result = submit(int(guess))
        submit_count += 1
        
        if result == "4S 0B":
            return int(guess)
        
        candidates = [
            candidate
            for candidate in candidates
            if get_score(guess, candidate) == result
        ]
    
    if len(candidates) == 1:
        return int(candidates[0])
    
    return 0