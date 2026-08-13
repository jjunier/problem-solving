from itertools import product


def solution(word):
    """
    Args:
        word(String): 알파벳 모음(A, E, I, O, U)으로 이루어진 문자열

    Returns
        (Int): 문자열이 정해진 규칙에서의 사전 속 몇 번째에 위치하는 지 나타내는 정수
    """
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []

    for length in range(1, 6):
        for combination in product(vowels, repeat=length):
            current_word = ''.join(combination)
            words.append(current_word)

    words.sort()

    return words.index(word) + 1