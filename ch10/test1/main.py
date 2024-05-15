def get_character_record(name, server, level, rank):
    result = {
        "name" : name,
        "server" : server,
        "level" : level,
        "rank" : rank,
        "id" : f"{name}#{server}"
    }

    return result
    
