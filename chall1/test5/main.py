def area_sum(rectangles):
    sum = 0

    for i in range(0, len(rectangles)):
        sum += rectangles[i]["height"] * rectangles[i]["width"]

    return sum