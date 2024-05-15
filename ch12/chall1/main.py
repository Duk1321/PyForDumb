def purchase(price, money_available):
    if money_available >= price:
        return money_available - price
    else:
        raise Exception("not enough money")
