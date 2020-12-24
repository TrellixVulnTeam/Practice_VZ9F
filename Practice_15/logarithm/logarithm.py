import math

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        return None
    return math.log(b, a)

def ln(b):
    if b <= 0: return None
    return math.log(b)

def lg(b):
    if b <= 0: return None
    return math.log10(b)