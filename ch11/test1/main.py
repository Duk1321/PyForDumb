def remove_duplicates(spells):
    spellSet = set()
    result = []
    
    for i in range(0, len(spells)):
        spellSet.add(spells[i])

    for spells in spellSet:
        result.append(spells)

    return result
