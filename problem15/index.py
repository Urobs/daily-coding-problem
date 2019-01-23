import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            random_element = e
        
        elif random.randint(1, i + 1) == 1:  # 随便挑一个数概率都为1/i
            random_element = e
    return random_element