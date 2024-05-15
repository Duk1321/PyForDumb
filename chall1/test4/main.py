def factorial(num):
    result = 1

    for i in range(num, 1, -1):
        result = result * i
    
    return result
