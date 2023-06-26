def divide_land_for_equal_squared_fields(width, height):
    print(width, height)
    if width % height == 0 or height % width == 0:
        min_len = min(width, height)
        return (min_len, min_len)
    
    # get min length
    min_len = 0
    max_len = 0
    if width < height:
        min_len = width
        max_len = height
    else:
        min_len = height
        max_len = width
    square_nbs = max_len // min_len
    return divide_land_for_equal_squared_fields(max_len - (square_nbs * min_len), min_len)
    