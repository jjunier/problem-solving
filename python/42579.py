def solution(genres, plays):
    """
    Args:
        genres: 노래의 장르를 나타내는 문자열 리스트 (List)
        plays:  노래별 재생 횟수를 나타내는 정수 배열 (List)

    Returns:
        (List):  베스트 앨범에 들어갈 노래의 고유 번호
    """
    genre_total = {}
    genre_songs = {}
    
    for index, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_total:
            genre_total[genre] = 0
            genre_songs[genre] = []
            
        genre_total[genre] += play
        genre_songs[genre].append((index, play))
        
    sorted_genres = sorted(
        genre_total,
        key=lambda genre: genre_total[genre],
        reverse=True
    )
            
    answer = []
    
    for genre in sorted_genres:
        sorted_songs = sorted(
            genre_songs[genre],
            key=lambda song: (-song[1], song[0])
        )
        
        for index, play in sorted_songs[:2]:
            answer.append(index)
            
    return answer