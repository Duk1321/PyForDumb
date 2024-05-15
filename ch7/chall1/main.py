def check_parking_meter(time_parked, time_purchased):
    result = ""
    if time_parked >= time_purchased:
        result = "overtime charged"
    else:
        result = "no charges yet"
    return result