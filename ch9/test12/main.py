def get_champion_slices(champions):
    first_slice = champions[2:]
    second_slice = champions[:-2]
    last_slice = champions[::2]
    return first_slice, second_slice, last_slice
