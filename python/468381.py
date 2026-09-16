UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

ROW_MOVE = [-1, 1, 0, 0]
COL_MOVE = [0, 0, -1, 1]

OPPOSITE_SIDE = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT,
}

TRACK_ROUTE = {
    1: {LEFT: RIGHT, RIGHT: LEFT},
    2: {UP: DOWN, DOWN: UP},
    4: {LEFT: UP, UP: LEFT},
    5: {UP: RIGHT, RIGHT: UP},
    6: {DOWN: RIGHT, RIGHT: DOWN},
    7: {LEFT: DOWN, DOWN: LEFT},
}

def count_routes(
    board,
    placed_tracks,
    row,
    col,
    entry_side,
    passed_track_count,
    required_track_count
):
    if board[row][col] == -1:
        return 0

    row_count = len(board) - 2
    col_count = len(board[0]) - 2
    current_track = board[row][col]

    # 목적지에 도착한 경우
    if row == row_count and col == col_count:
        return int(
            passed_track_count == required_track_count
            and current_track in TRACK_ROUTE
            and entry_side in TRACK_ROUTE[current_track]
        )

    route_count = 0

    # 기존 일반 선로
    if current_track in TRACK_ROUTE:
        if entry_side not in TRACK_ROUTE[current_track]:
            return 0

        exit_side = TRACK_ROUTE[current_track][entry_side]

        next_row = row + ROW_MOVE[exit_side]
        next_col = col + COL_MOVE[exit_side]
        next_entry_side = OPPOSITE_SIDE[exit_side]

        route_count += count_routes(
            board,
            placed_tracks,
            next_row,
            next_col,
            next_entry_side,
            passed_track_count + 1,
            required_track_count
        )

    # 기존 3번 선로
    elif current_track == 3:
        visit_state = placed_tracks[row][col]
        is_horizontal = entry_side in (LEFT, RIGHT)

        if visit_state == 0:
            placed_tracks[row][col] = 8 if is_horizontal else 9

            exit_side = OPPOSITE_SIDE[entry_side]
            next_row = row + ROW_MOVE[exit_side]
            next_col = col + COL_MOVE[exit_side]
            next_entry_side = OPPOSITE_SIDE[exit_side]

            route_count += count_routes(
                board,
                placed_tracks,
                next_row,
                next_col,
                next_entry_side,
                passed_track_count + 1,
                required_track_count
            )

            placed_tracks[row][col] = 0

        elif (
            (visit_state == 8 and not is_horizontal)
            or
            (visit_state == 9 and is_horizontal)
        ):
            placed_tracks[row][col] = 10

            exit_side = OPPOSITE_SIDE[entry_side]
            next_row = row + ROW_MOVE[exit_side]
            next_col = col + COL_MOVE[exit_side]
            next_entry_side = OPPOSITE_SIDE[exit_side]

            route_count += count_routes(
                board,
                placed_tracks,
                next_row,
                next_col,
                next_entry_side,
                passed_track_count + 1,
                required_track_count
            )

            placed_tracks[row][col] = visit_state

    # 빈칸
    elif current_track == 0:

        # 이전 탐색에서 이미 선로를 설치한 빈칸
        if placed_tracks[row][col] != 0:
            visit_state = placed_tracks[row][col]
            is_horizontal = entry_side in (LEFT, RIGHT)

            if (
                (visit_state == 8 and not is_horizontal)
                or
                (visit_state == 9 and is_horizontal)
            ):
                placed_tracks[row][col] = 10

                exit_side = OPPOSITE_SIDE[entry_side]
                next_row = row + ROW_MOVE[exit_side]
                next_col = col + COL_MOVE[exit_side]
                next_entry_side = OPPOSITE_SIDE[exit_side]

                route_count += count_routes(
                    board,
                    placed_tracks,
                    next_row,
                    next_col,
                    next_entry_side,
                    passed_track_count + 1,
                    required_track_count
                )

                placed_tracks[row][col] = visit_state

        # 처음 방문하는 빈칸
        else:
            for candidate_track in range(1, 8):
                placed_tracks[row][col] = candidate_track

                # 3번 선로
                if candidate_track == 3:
                    is_horizontal = entry_side in (LEFT, RIGHT)
                    placed_tracks[row][col] = 8 if is_horizontal else 9

                    exit_side = OPPOSITE_SIDE[entry_side]
                    next_row = row + ROW_MOVE[exit_side]
                    next_col = col + COL_MOVE[exit_side]
                    next_entry_side = OPPOSITE_SIDE[exit_side]

                    route_count += count_routes(
                        board,
                        placed_tracks,
                        next_row,
                        next_col,
                        next_entry_side,
                        passed_track_count,
                        required_track_count + 1
                    )

                # 일반 선로
                elif entry_side in TRACK_ROUTE.get(candidate_track, {}):
                    exit_side = TRACK_ROUTE[candidate_track][entry_side]

                    next_row = row + ROW_MOVE[exit_side]
                    next_col = col + COL_MOVE[exit_side]
                    next_entry_side = OPPOSITE_SIDE[exit_side]

                    route_count += count_routes(
                        board,
                        placed_tracks,
                        next_row,
                        next_col,
                        next_entry_side,
                        passed_track_count,
                        required_track_count
                    )

                placed_tracks[row][col] = 0

    return route_count


def solution(grid):
    """
    Args:
        grid(Matrix): n * m 격자 내 위치한 빈칸, 선로, 장애물의 정보가 담긴 이차원 리스트

    Returns:
        (Int): 끊어진 선로를 잇는 모든 경우의 수
    """
    row_count = len(grid)
    col_count = len(grid[0])

    board = [
        [-1] * (col_count + 2)
        for _ in range(row_count + 2)
    ]

    placed_tracks = [
        [0] * (col_count + 2)
        for _ in range(row_count + 2)
    ]

    required_track_count = 0

    for row in range(row_count):
        for col in range(col_count):
            board[row + 1][col + 1] = grid[row][col]

            if grid[row][col] == 3:
                required_track_count += 2

            elif grid[row][col] > 0:
                required_track_count += 1

    return count_routes(
        board,
        placed_tracks,
        1,
        1,
        LEFT,
        1,
        required_track_count
    )