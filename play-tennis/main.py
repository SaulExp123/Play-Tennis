def run(points: str) -> str:
    SETS_FOR_TIEBREAK = 6
    result = ''
    sets_a = 0
    sets_b = 0
    points_a = 0
    points_b = 0
    tiebreak = False
    a_win_tiebreak = False
    b_win_tiebreak = False

    for char in points:
        if sets_a == SETS_FOR_TIEBREAK and sets_b == SETS_FOR_TIEBREAK:
            tiebreak = True
        if tiebreak:
            if char == 'A':
                points_a += 1
            else:
                points_b += 1
            if points_a >= 7 and points_a - points_b >= 2:
                a_win_tiebreak = True
                points_a = 0
                points_b = 0
            elif points_b >= 7 and points_b - points_a >= 2:
                b_win_tiebreak = True
                points_a = 0
                points_b = 0

            if a_win_tiebreak:
                result += f'{sets_a + 1}-{sets_b} '
                sets_a = 0
                sets_b = 0
                a_win_tiebreak = False
                tiebreak = False
            elif b_win_tiebreak:
                result += f'{sets_a}-{sets_b + 1} '
                sets_a = 0
                sets_b = 0
                b_win_tiebreak = False
                tiebreak = False

        else:
            if char == 'A':
                points_a += 1
            else:
                points_b += 1
            if points_a >= 4 and points_a - points_b >= 2:
                sets_a += 1
                points_a = 0
                points_b = 0
            elif points_b >= 4 and points_b - points_a >= 2:
                sets_b += 1
                points_a = 0
                points_b = 0
            if sets_a >= 6 and sets_a - sets_b >= 2:
                result += f'{sets_a}-{sets_b} '
                sets_a = 0
                sets_b = 0
            elif sets_b >= 6 and sets_b - sets_a >= 2:
                result += f'{sets_a}-{sets_b} '
                sets_a = 0
                sets_b = 0

    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
