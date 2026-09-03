from collections import deque

def normalize(shape):
    min_x = min(x for x, y in shape)
    min_y = min(y for x, y in shape)
    
    normalized = []
    
    for x, y in shape:
        normalized.append((x - min_x, y - min_y))
        
    normalized.sort()
    
    return normalized

def extract_shapes(board, target):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    shapes = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == target and not visited[i][j]:
                queue = deque()
                queue.append((i, j))

                
                visited[i][j] = True
                
                shape = []
                
                while queue:
                    x, y = queue.popleft()
                    shape.append((x, y))
                    
                    for direction in range(4):
                        nx = x + dx[direction]
                        ny = y + dy[direction]
                        
                        if(0 <= nx < n and 0 <= ny < n
                          and not visited[nx][ny]
                          and board[nx][ny] == target):
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            
                shapes.append(normalize(shape))
                
    return shapes

def rotate(shape):
    rotated = []
    
    for x, y in shape:
        rotated.append((y, -x))
        
    return normalize(rotated)
                            
def solution(game_board, table):
    """
    Args:
        game_board(Matrix): 현재 게임 보드의 상태를 나타내는 이차원 리스트
        table(Matrix): 테이블 위에 놓인 퍼즐 조각의 상태를 나타내는 이차원 리스트

    Returns:
        (Int): 규칙에 맞게 최대한 퍼즐 조각을 채운 갯수
    """
    blanks = extract_shapes(game_board, 0)
    pieces = extract_shapes(table, 1)
    
    used = [False] * len(pieces)
    
    answer = 0
    
    for blank in blanks:
        for i in range(len(pieces)):
            if used[i]:
                continue
                
            if len(blank) != len(pieces[i]):
                continue
                
            current_piece = pieces[i]
            
            for _ in range(4):
                if blank == current_piece:
                    used[i] = True
                    answer += len(blank)
                    break
                    
                current_piece = rotate(current_piece)
                
            if used[i]:
                break
                
    return answer