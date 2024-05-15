def double_string(string):
    result = []
    for i in range(0, len(string)):
        if isinstance(string[i], str):
            result.append(string[i] * 2)
    full = "".join(result)

    return full