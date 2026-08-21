from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    """
    Args:
        rectangle(Matrix): 직사각형의 좌측 하단의 x, y 좌표 우측 상단의 x, y 좌표가 담긴 이차원 리스트
        characterX: 초기 케릭터의 x 좌표
        characterY: 초기 케릭터의 y 좌표
        itemX: 주워야 할 아이템의 x 좌표
        itemY: 주워야 할 아이템의 y 좌표

    Returns:
        (Int): 케릭터가 아이템을 줍기 위한 최단 거리
    """
    board = [[0] * 102 for _ in range(102)]

    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] = 1

    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 0

    start_x = characterX * 2
    start_y = characterY * 2

    target_x = itemX * 2
    target_y = itemY * 2

    queue = deque()
    queue.append((start_x, start_y, 0))

    visited = [[False] * 102 for _ in range(102)]
    visited[start_x][start_y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y, distance = queue.popleft()

        if x == target_x and y == target_y:
            return distance // 2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < 102
                and 0 <= ny < 102
                and not visited[nx][ny]
                and board[nx][ny] == 1
            ):
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))