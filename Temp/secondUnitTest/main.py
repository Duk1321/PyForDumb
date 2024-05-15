def take_magic_damage(health, resist, amp, spell_power):
    result = health - (spell_power * amp) + resist
    return result 
