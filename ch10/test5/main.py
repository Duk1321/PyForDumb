def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    result = None
    for name in enemies_dict:
        if max_so_far < enemies_dict[name]:
            max_so_far = enemies_dict[name]
            result = name
    return result