def count_unique_climb_ways(distance, steps):
    count = 0
    for step in steps:
        if distance - step  == 0:
            count += 1
        elif distance - step > 0:
            count += count_unique_climb_ways(distance - step, steps)

    return count