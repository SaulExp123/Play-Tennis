def run(points: str) -> str:
    GAMES_FOR_TIEBREAK = 6
    MIN_DIFF_WIN = 2
    POINTS_FOR_GAME = 4
    GAMES_FOR_SET = 6
    GAMES_FOR_WIN_TIEBREAK = 7

    result = ''
    games_a = 0
    games_b = 0
    points_a = 0
    points_b = 0
    tiebreak = False

    for player in points:
        if games_a == GAMES_FOR_TIEBREAK and games_b == GAMES_FOR_TIEBREAK:
            tiebreak = True
        match player:
            case 'A':
                points_a += 1
            case 'B':
                points_b += 1
            case _:
                continue
        if not tiebreak:
            if points_a >= POINTS_FOR_GAME and points_a - points_b >= MIN_DIFF_WIN:
                games_a += 1
                points_a = 0
                points_b = 0
            elif points_b >= POINTS_FOR_GAME and points_b - points_a >= MIN_DIFF_WIN:
                games_b += 1
                points_a = 0
                points_b = 0
            if (games_a >= GAMES_FOR_SET and games_a - games_b >= MIN_DIFF_WIN) or (
                games_b >= GAMES_FOR_SET and games_b - games_a >= MIN_DIFF_WIN
            ):
                result += f'{games_a}-{games_b} '
                games_a = 0
                games_b = 0
        else:
            if points_a >= GAMES_FOR_WIN_TIEBREAK and points_a - points_b >= MIN_DIFF_WIN:
                games_a += 1
            elif points_b >= GAMES_FOR_WIN_TIEBREAK and points_b - points_a >= MIN_DIFF_WIN:
                games_b += 1
            if games_a == GAMES_FOR_WIN_TIEBREAK or games_b == GAMES_FOR_WIN_TIEBREAK:
                result += f'{games_a }-{games_b} '
                games_a = 0
                games_b = 0
                points_a = 0
                points_b = 0
                tiebreak = False
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
