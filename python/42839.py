from itertools import permutations

def solution(numbers):
    candidates = set()
    
    for length in range(1, len(numbers) + 1):
        for permutation in permutations(numbers, length):
            number = int(''.join(permutation))
            candidates.add(number)
            
    prime_count = 0
    
    for number in candidates:
        if number < 2:
            continue
            
        is_prime = True
        
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
                
        if is_prime:
            prime_count += 1
                
    return prime_count