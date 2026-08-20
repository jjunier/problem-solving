from collections import deque

def solution(maps):
    """
    Args:
        maps(Matrix): 게임 맵의 상태인 벽의 유무가 0/1로 이루어진 n * m 크기의 이차원 배열

    Returns:
        (Int): 케릭터의 상대팀 진영에 도착하기 위해 지나가야 하는 칸 갯수의 최솟값
    """
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    
    if maps[n-1][m-1] == 1:
        return -1
    
    return maps[n-1][m-1]