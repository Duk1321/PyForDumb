def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    # don't touch above this line

    old_index = []
    new_index = []

    for i in range(0, len(old_character_levels)):
        if old_character_levels[i] < new_character_levels[i]:
            old_index.append(old_character_levels[i])
            new_index.append(new_character_levels[i])

    print(old_index)
    print(new_index)


# don't touch below this line


def test():
    print("Character level increased at indexes:")
    check_character_levels()
    print("=====================================")


def main():
    test()


main()
