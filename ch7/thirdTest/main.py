def can_withstand_blow(hero_armor, enemy_damage):
    tankable = hero_armor >= enemy_damage
    return tankable
