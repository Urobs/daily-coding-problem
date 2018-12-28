def car(pair):
    return pair(lambda x, y: x)

def cdr(pair):
    return pair(lambda x, y: y)