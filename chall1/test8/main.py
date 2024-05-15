def join_strings(strings):
    if len(strings) == 0:
        return ""
    else:
        result = strings[0]

        for i in range(1, len(strings)):
            result += f",{strings[i]}"

        return result
