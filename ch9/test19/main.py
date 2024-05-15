def filter_messages(messages):
    result1 = []
    result2 = []

    for i in range(0, len(messages)):
        sliced = messages[i].split()
        counter = 0
        filterList = []
        for j in range(0, len(sliced)):
            if sliced[j] != "dang":
                filterList.append(sliced[j])
            else:
                counter += 1
        full = " ".join(filterList)
        result1.append(full)
        result2.append(counter)
       
    return result1, result2
