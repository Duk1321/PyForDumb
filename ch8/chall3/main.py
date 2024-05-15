def calculate_experience_points(level):
    total_exp = 0

    for i in range(0, level):
        total_exp = total_exp + i*5
    return total_exp
