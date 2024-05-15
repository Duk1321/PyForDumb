def find_missing_ids(first_ids, second_ids):
    nonDup = set()
    result = []

    for i in range(0, len(first_ids)):
        nonDup.add(first_ids[i])

    for number in nonDup:
        if number not in second_ids:
            result.append(number)
    
    return result
