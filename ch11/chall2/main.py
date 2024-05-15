def count_vowels(text):
    spaceCounter = 0
    check = []
    result = set()
    check[:] = text
    for i in range(0, len(check)):
        if check[i] == "A" or check[i] == "a" or check[i] == "E" or check[i] == "e" or check[i] == "I" or check[i] == "i" or check[i] == "O" or check[i] == "o" or check[i] == "U" or check[i] == "u":
            spaceCounter += 1
            result.add(check[i])
    return spaceCounter, result

