def has_enough_gas(gallons_in_car, miles_one_way, miles_per_gallon):
    gallons_needed = (miles_one_way * 2) / miles_per_gallon
    result = True
    if gallons_in_car >= gallons_needed:
        result = True
    else:
        result = False
    return result
