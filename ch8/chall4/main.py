def is_prime(number):
    check = 0
    if number <= 1:
        return False
    else:
        for i in range(number, 0, -1):
            if number % i == 0:
                check += 1
        if check > 2:
            return False
        else:
            return True
