def smelt_ore():
    inventory = ["Healing Potion", "Iron Ore", "Bread", "Shortsword"]
    print(f"Inventory: {inventory}")

    # don't touch above this line

    for i in range (0,len(inventory) - 1):
        if inventory[i] == "Iron Ore":
            inventory[i] = "Iron Bar"

    # don't touch below this line

    return inventory


def test():
    inventory = smelt_ore()
    print(f"Smelting ore: {inventory}")
    print("=====================================")


def main():
    test()


main()
