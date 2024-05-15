def player_status(health):
    result = ""
    if health <= 0:
        result = "dead"
    elif health <= 5:
        result = "injured"
    else:
        result = "healthy"
    return result