import random

def monte_carlo_estimate(n):
    count_total = n
    count_circle = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (pow((x-0.5), 2) + pow((y-0.5), 2))**0.5 <= 0.5: 
            count_circle += 1 
    return round(count_circle / count_total / 0.25, 3)