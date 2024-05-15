def remove_duplicates(lst):
    resultSet = set()
    for i in range(0, len(lst)):
        resultSet.add(lst[i])

    return resultSet
