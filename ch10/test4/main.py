def count_enemies(enemy_names):
    a = {}
    for names in enemy_names:
        a[names] = enemy_names.count(names)
    return a

