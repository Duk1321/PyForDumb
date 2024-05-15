def get_first_item(items):
    result = ""
    if len(items) == 0:
        result = "ERROR"
    else:
        result = items[0]
    return result
